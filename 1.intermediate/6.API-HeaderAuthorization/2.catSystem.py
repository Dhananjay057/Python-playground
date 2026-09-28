# -- print("Hi, Provide login and password")

# checking whether login and password are correct
# assuming : login completed correctly
# we retrieve from database: userId and username for further referrence


import requests
import json
from pprint import pprint
import webbrowser
import settings

headers = {
    "x-api-key" : settings.apiKey
}

def get_json_content_from_repsonse(response):
    try:
        content = response.json()
    except json.decoder.JSONDecodeError:
        print("Not the JSON content")
    else:
        return content

def get_favorite_cats(userId):
    params = {
        "subId" : userId
    }
    r = requests.get("https://api.thecatapi.com/v1/favourites", params=params, headers = headers)

    return get_json_content_from_repsonse(r)

def get_random_cats():

    r = requests.get("https://api.thecatapi.com/v1/images/search", headers = headers)

    return get_json_content_from_repsonse(r)[0]

userId = "dj047"
userName = "Dhananjay"
print("Hi " + userName)
favouriteCats = get_favorite_cats(userId)
print("your favourite Cats are :", favouriteCats)

randomCat = get_random_cats()
print(randomCat['url'])
# webbrowser.open_new_tab(randomCat['url'])



