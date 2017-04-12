#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    import sys
    myurl = sys.argv[1]
    r = requests.get(myurl)
    print(r.headers.get('X-Request-Id'))
