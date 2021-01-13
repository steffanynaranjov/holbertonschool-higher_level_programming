#!/usr/bin/python3
"""takes in a URL and an email, sends a POST"""
if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value).encode('ascii')
    reque = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(reque) as response:
        print(response.read().decode('utf-8'))
