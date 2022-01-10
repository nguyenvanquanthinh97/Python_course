import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import requests

proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token, http_client=proxy_client)

hour = int(os.environ['HOUR_NOW'])
def transform_time_msg(number):
    global hour
    result = hour + number
    if result >= 24:
        result -= 24
        return f"{result}:00 tomorrow"
    return f"{result}:00 today"

    
api_key = os.environ['OPEN_WEATHER_API']
params = {
    "lat": 10.823099,
    "lon": 106.629662,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
open_weather_api = "https://api.openweathermap.org/data/2.5/onecall"

response = requests.get(open_weather_api, params=params)
response.raise_for_status()

weather_data = response.json()
weather_data_slice = weather_data.get("hourly")[:24]

is_raining = False
raining_messages = []
for hour in range(len(weather_data_slice)):
    weather_at = weather_data_slice[hour]["weather"][0]
    if weather_at.get("id") < 700:
        is_raining = True
        description = weather_at.get("description")
        time_msg = transform_time_msg(hour)
        raining_messages.append(f"{time_msg}, detail: {description}.\n")

if is_raining:
    from_phone = os.environ['FROM_PHONE']
    to_phone = os.environ['TO_PHONE']
    message_body = "There will be rained in:\n" + "".join(raining_messages)        
    message = client.messages.create(body=message_body, from_=from_phone, to=to_phone)
