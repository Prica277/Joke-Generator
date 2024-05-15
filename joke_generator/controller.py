"""
controller.py
by Prica277
Python code to make API connections.
"""

import requests as re

base_url = "https://official-joke-api.appspot.com/jokes/"


def make_api_call(type_of_joke, amount_of_jokes):
    #building the url
    endpoint = type_of_joke
    if amount_of_jokes == "1":
        endpoint += "/random"
    else:
        endpoint += "/ten"
    url = base_url + endpoint
    response = re.get(url)

    
    if response.ok:
        output = get_output(response)
    else:
        output = f"There was an error: {response.status_code}"
    print(output)

def get_output(response):
    output = ""
    jokes = response.json()
    for joke in jokes:
        setup = joke.get("setup")
        print(setup)
        punchline = joke.get("punchline")
        print(punchline)
    return output

if __name__ == "__main__":
    make_api_call("programming", "1")
    

