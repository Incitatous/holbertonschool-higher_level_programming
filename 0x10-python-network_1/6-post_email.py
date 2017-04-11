#!/usr/bin/python3
import requests
import sys
myurl = sys.argv[1]
email = sys.argv[2]
data = {'email': email}
r = requests.post(myurl, data)
print(r.text)
