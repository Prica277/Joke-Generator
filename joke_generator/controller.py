"""
controller.py
by Prica277
Python code to make API connections.
"""

import requests as re
import interface as interface

base_url = "https://official-joke-api.appspot.com"
default_endpoint = "/random_joke"
ten_endpoint = "/random_ten"
programming_endpoint = "/jokes/programming/random"
programming_ten_endpoint = "/jokes/programming/ten"
knock_endpoint = "/jokes/knock-knock/random"
knock_ten_endpoint = "/jokes/knock-knock/ten"


#building the url
url = base_url + default_endpoint
response = re.get(url)

if response.ok:
    print(response.text)
else:
    print(f"There was an error: {response.status_code}")

