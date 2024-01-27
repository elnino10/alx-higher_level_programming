#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
"""
if __name__ == "__main__":
    import sys

    import requests

    url = sys.argv[1]
    res = requests.get(url)
    x_request_id = res.headers.get("X-Request-Id")
    print(x_request_id)
