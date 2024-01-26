#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body
of the response (decoded in utf-8)
"""
if __name__ == "__main__":
    import sys
    from urllib import parse, request

    url = sys.argv[1]
    email_arg = {"email": sys.argv[2]}

    # encode parameter to utf-8
    email_data = parse.urlencode(email_arg).encode("utf-8")
    req = request.Request(url, email_data)
    with request.urlopen(req) as response:
        res = response.read().decode("utf-8")
        print(res)
