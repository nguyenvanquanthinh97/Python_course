import requests

def fetch_data():
    response = requests.get("https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean")
    response.raise_for_status()

    data = response.json().get("results")
    return data

question_data = fetch_data()