import requests
import json
from pprint import pprint
import settings
import webbrowser

header = {
    "x-api-key": settings.apiKey
    }

r = requests.get("https://api.thecatapi.com/v1/favourites", headers = header)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Not the JSON content")
else:
    print(content)