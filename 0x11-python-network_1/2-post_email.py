#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body
of the response (decoded in utf-8)
"""
if __name__ == "__main__":
    import sys
    import urllib.parse
    import urllib.request

    url = sys.argv[1]
    email_arg = {"email": sys.argv[2]}

    # encode parameter to utf-8
    email_data = urllib.parse.urlencode(email_arg).encode("ascii")
    req = urllib.request.Request(url, email_data)
    with urllib.request.urlopen(req) as response:
        res = response.read().decode("utf-8")
        print(res)
