#!/usr/bin/python3
"""
script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and finally displays
the body of the response
"""
if __name__ == "__main__":
    import sys

    import requests

    url = sys.argv[1]
    email_arg = {"email": sys.argv[2]}

    res = requests.post(url, email_arg)
    print(res)
