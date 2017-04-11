#!/usr/bin/python3
if __name__ == "__main__":
    import urllib.request
    import sys
    from urllib.error import URLError, HTTPError
    myurl = sys.argv[1]
    try:
        with urllib.request.urlopen(myurl) as response:
            html = response.read()
            utf = html.decode('utf-8')
        print("{}".format(utf))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
