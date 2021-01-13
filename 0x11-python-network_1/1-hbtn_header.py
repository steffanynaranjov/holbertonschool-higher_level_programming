#!/usr/bin/python3
"""displays the value of the X-Request-Id"""
if __name__ == '__main__':
    import urllib.request
    import sys
    reque = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(reque) as response:
        print(response.info().get("X-Request-Id"))
