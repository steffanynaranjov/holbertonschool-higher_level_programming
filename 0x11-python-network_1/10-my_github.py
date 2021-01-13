#!/usr/bin/python3
"""Write a Python script that takes your Github credentials (username and
password) and uses the Github API to display your id"""
if __name__ == '__main__':
    import requests
    import sys
    authorize = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get('https://api.github.com/user', auth=authorize)
    try:
        print(response.json().get('id'))
    except ValueError:
        print("Not a valid JSON")
