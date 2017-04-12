#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    import sys
    myurl = sys.argv[1]
    r = requests.get(myurl)
    if r.status_code == requests.codes.ok:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
