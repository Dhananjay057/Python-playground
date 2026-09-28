"""
JSON Placeholder
"""

import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")
# print(response.text)
print(type(response.text)) # <class 'str'>

result = json.loads(response.text)

print(type(result))
print(result[0])
