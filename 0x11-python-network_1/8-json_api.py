#!/usr/bin/python3

import sys
import requests

"""Sends a POST request to http://0.0.0.0:5000/search_user with a given alphabet

Usage: ./8-json_api.py <letter>
  - The alphabet is sent as the value of the variable `q`.
  - If no alphabet is provided, sends `q=""`.
"""

if __name__ == "__main__":

    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
