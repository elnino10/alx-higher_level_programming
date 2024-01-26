## Network #0 README

The Web, often known as the Internet, is a vast distributed client/server information system.
Numerous site apps, including file transfers, email, streaming audio and video, site browsing, and more, operate simultaneously.  These programs need to agree on a particular application-level protocol, like `HTTP`, `FTP`, `SMTP`, `POP`, and so on, in order for the client and server to communicate properly.

## Overview
This project topic delves into the basics of networking and the http request-response cycle. It further explains through the provided resources how http protocol behaves under the hood. The topic also has a glance at `cURL` pronounced "client URL", how it is used to interact with the server and shows how powerful a tool cURL is.

## Learning Objectives
### General
- What a URL is
- What HTTP is
- How to read a URL
- The scheme for a HTTP URL
- What a domain name is
- What a sub-domain is
- How to define a port number in a URL
- What a query string is
- What an HTTP request is
- What an HTTP response is
- What HTTP headers are
- What the HTTP message body is
- What an HTTP request method is
- What an HTTP response status code is
- What an HTTP Cookie is
- How to make a request with cURL
- What happens when you type google.com in your browser (Application level)

## Resources
- [HTTP (HyperText Transfer Protocol)](https://intranet.alxswe.com/rltoken/rAon_EpQ6PGl8N0plySn4A)
- [HTTP Cookies](https://intranet.alxswe.com/rltoken/MhVCl_0oviQldWPn5oX-NQ)

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- A README.md file, at the root of the folder of the project, is mandatory
- All your scripts will be tested on `Ubuntu 20.04 LTS`
- All your Bash scripts should be exactly 3 lines long (wc -l file should print 3)
- All your files should end with a new line
- All your files must be executable
- The first line of all your bash files should be exactly `#!/bin/bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing
- All curl commands must have the option `-s` (silent mode)
- All your files will be interpreted/compiled on `Ubuntu 20.04` LTS using python3 (version 3.8.5)
- The first line of all your Python files should be exactly `#!/usr/bin/python3`
- Your code should use the pycodestyle (version 2.8.*)
- All your modules should be documented: `python3 -c 'print(__import__("my_module").__doc__)'`
- All your classes should be documented: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
- All your functions (inside and outside a class) should be documented: `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Example task
```
Write a simple Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

  - The size must be displayed in bytes
  - You have to use curl
```

### Example solution
```
#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sI "$1" | sed -ne 's/Content-Length: //p'
```
