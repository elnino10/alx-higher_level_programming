#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""
if __name__ == "__main__":
    import sys
    from urllib import request

    url = sys.argv[1]

    data = request.Request(url)
    with request.urlopen(data) as response:
        print(response.read().decode("utf-8"))
