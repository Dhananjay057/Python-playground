"""
prettty printer (pprint) - A pretty printer is a tool that takes data and formats it in a way that is easy to read and understand. It can be used to format code, data structures, or any other type of information that needs to be presented in a clear and organized manner.
"""

import json

movie = {
    "title": "But I won't do it!",
    "release_year": 1969,
    "won_oscar": True,
    "actors": ["Arkadiusz Wlodarczyk", "Wiolletta Wlodarczyk"],
    "budget": None,
    "credits": {
        "director": "Arkadiusz Wlodarczyk",
        "writer": "Alan Burger",
        "animator": "Anime Animatrix"
    }
}
print(type(movie)) # <class 'dict'>

encoded_movies = json.dumps(movie, ensure_ascii=False, indent=4, sort_keys=True)
print(encoded_movies)

print(type(encoded_movies)) # <class 'str'>