#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    import sys
    character = sys.argv[1]
    myurl = "https://swapi.co/api/people/?search=" + character
    r = requests.get(myurl)
    count = r.json().get("count")
    res = r.json().get("results")
    print("Number of result: {}".format(count))
    for i in res:
        print(i.get("name"))
