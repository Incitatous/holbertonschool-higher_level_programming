#!/usr/bin/python3
import requests
myurl = "https://intranet.hbtn.io/status"
r = requests.get(myurl)
print("Body response:")
print("\t- type: {}".format(type(r.text)))
print("\t- content: {}".format(r.text))
