#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
if __name__ == "__main__":
    import sys

    import requests

    username = sys.argv[1]
    password = sys.argv[2]
    payload = {"login": username}
    url = f"https://api.github.com/user"

    res = requests.get(url, params=payload, auth=(username, password))
    json_data = res.json()

    try:
        print(json_data['id'])
    except KeyError:
        print("None")
