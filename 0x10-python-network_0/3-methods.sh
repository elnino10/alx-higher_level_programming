#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept
curl -sIX OPTIONS "$1" | sed -ne 's/Allow: //p'
