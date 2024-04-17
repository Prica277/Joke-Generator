"""
controller.py
by Prica277
Python code to make API connections.
"""

import requests as re

base_url = "https://official-joke-api.appspot.com"
endpoint = "/random_joke"

#building the url
url = base_url + endpoint
response = re.get(url)

if response.ok:
    print(response.text)
else:
    print(f"There was an error: {response.status_code}")

