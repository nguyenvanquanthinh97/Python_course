import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# Throw exception if get error statuscode
response.raise_for_status()

# get data type 'Dict'
print(type(response.json()))

params = {
    "lat": "10.7815271",
    "lng": "106.6409313"
}
response = requests.get("https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()

print(response.json())