#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
if __name__ == "__main__":
    import requests

    res = requests.get("https://alx-intranet.hbtn.io/status")
    print(f"Body response:\n\t- type: {type(res.text)}\n\t- content: {res.text}")
