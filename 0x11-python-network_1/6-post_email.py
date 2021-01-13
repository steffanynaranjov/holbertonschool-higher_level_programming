#!/usr/bin/python3
"""POST request to the passed URL with the email as a parameter,
and finally displays the body of the response"""
if __name__ == '__main__':
    import requests
    import sys
    value = {'email': sys.argv[2]}
    request = requests.post(sys.argv[1], data=value)
    print(request.text)
