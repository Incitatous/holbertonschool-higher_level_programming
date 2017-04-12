#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    import sys
    if len(sys.argv) != 2 or not sys.argv[1].isalpha():
        print("No result")
    else:
        q = sys.argv[1]
        myurl = 'http://0.0.0.0:5000/search_user'
        r = requests.post(myurl, data={'q': q})
        myid = r.json().get("id")
        name = r.json().get("name")
        print("[{}] {}".format(myid, name))
