import requests
import json
import pprint
import webbrowser

params = {
    "site" : "stackoverflow",
    "sort" : "votes",
    "min" :15,
    "order" :"desc",
    "fromdate":"2019-09-03",
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
        