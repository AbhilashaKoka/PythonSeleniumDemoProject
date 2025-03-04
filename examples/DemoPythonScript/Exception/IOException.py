import requests
from requests.exceptions import RequestException

try:
    response = requests.get('https://www.google.com/')
    response.raise_for_status()
    print(response.json())
except RequestException as e:
    print("An error occurred: ", e)
