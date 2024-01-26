#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
if __name__ == "__main__":
    import urllib.request

    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")

    with urllib.request.urlopen(req) as response:
        res = response.read()
        print(
            f"Body response:\n\t- type: {type(res)}"
            + f"\n\t- content: {res}\n\t- utf8 content: {res.decode('utf-8')}"
        )
