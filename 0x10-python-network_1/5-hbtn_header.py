#!/usr/bin/python3
import requests
import sys
myurl = sys.argv[1]
r = requests.get(myurl)
print(r.headers.get('X-Request-Id'))
