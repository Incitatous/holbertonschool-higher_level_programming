#!/usr/bin/python3
import requests
import sys
myurl = sys.argv[1]
email = sys.argv[2]
r = requests.post(myurl, data={'email': email})
print(r.text)
