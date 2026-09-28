import requests
import json
import webbrowser
from datetime import datetime, timedelta

timeBefore = timedelta(days=7)
startDate = datetime.today() - timeBefore

print(int(startDate.timestamp()))

params = {
    "site" : "stackoverflow",
    "sort" : "votes",
    "min" :15,
    "order" :"desc",
    "fromdate":int(startDate.timestamp()),
    "tagged":"python"
    }

response = requests.get("https://api.stackexchange.com/2.3/questions", params)
try:
    questions = response.json()
except json.decoder.JSONDecodeError:
    print("Data is not json")
else:
    for question in questions["items"]:
        webbrowser.open_new_tab(question["link"])

        