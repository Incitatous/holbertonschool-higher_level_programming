#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    import sys
    user = sys.argv[1]
    passwd = sys.argv[2]
    myurl = "https://api.github.com/user"
    r = requests.get((myurl), auth=(user, passwd))
    print(r.json().get("id"))
