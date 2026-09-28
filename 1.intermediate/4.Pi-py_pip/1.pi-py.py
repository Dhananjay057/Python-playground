"""
pip - pip installs packages - package installer
PyPi - Python Package index - list of external packages written in Python


WRITE a function that will open website provided as argument :-
create a list of websites
create a list of websites that DIDn't open properly (404)
save all these not opening websites into a file
save all websites that are opening into another file

"""

import requests

result = requests.get("https://www.google.com")
print(result)

websites = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.stackoverflow.com",
    "https://www.python.org",
    "https://www.example.com",
    "https://www.wikipedia.orghbfhb",
    "https://www.myreddit.com"
]

def filter_websites(websites):
    for website in websites:
        try:
            response = requests.get(website)
            if response.status_code == 200:
                with open("working_websites.txt", "a") as working_file:
                    working_file.write(website + "\n")
            else:
                with open("not_working_websites.txt", "a") as not_working_file:
                    not_working_file.write(website + "\n")
        except requests.exceptions.RequestException:
            with open("not_working_websites.txt", "a") as not_working_file:
                not_working_file.write(website + "\n")

filter_websites(websites)