#!/usr/bin/python3
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read())
