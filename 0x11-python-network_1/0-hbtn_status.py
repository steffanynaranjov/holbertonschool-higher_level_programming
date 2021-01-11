#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        resp = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(resp)))
        print('\t- content: {}'.format(resp))
        print('\t- utf8 content: {}'.format(resp.decode('UTF-8')))