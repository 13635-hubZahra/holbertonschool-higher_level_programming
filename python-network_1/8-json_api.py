#!/usr/bin/python3
"""
Sends a letter to a search API and handles the JSON response.
"""
import sys
import requests


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {'q': q}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        search_result = r.json()
        if not search_result:
            print("No result")
        else:
            print("[{}] {}".format(search_result.get('id'),
                                   search_result.get('name')))
    except ValueError:
        print("Not a valid JSON")
