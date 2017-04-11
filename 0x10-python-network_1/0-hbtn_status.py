#!/usr/bin/python3
if __name__ == "__main__":
    import urllib.request
    myurl = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(myurl) as response:
        html = response.read()
        utf = html.decode('utf-8')
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(utf))
