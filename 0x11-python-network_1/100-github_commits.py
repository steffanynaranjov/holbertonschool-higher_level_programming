#!/usr/bin/python3
"""The Holberton School staff evaluates candidates applying for
a back-end position with multiple technical challenges, like this one"""
if __name__ == '__main__':
    import requests
    import sys
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    try:
        response = requests.get(url)
        commits = response.json()
        for commit in commits[:10]:
            print("{}: {}".format(
                commit.get('sha'),
                commit.get('commit').get('author').get('name')))
    except ValueError:
        print("Not a valid JSON")
