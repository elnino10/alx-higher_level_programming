#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
if __name__ == "__main__":
    import sys

    import requests

    url = "http://0.0.0.0:5000/search_user"
    try:
        if len(sys.argv) < 2:
            var = {"q": ""}
        else:
            var = {"q": sys.argv[1]}
        res = requests.post(url, var)
        if res.json():
            print(f"[{res.json().id}] {res.json().name}")
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
