#!/usr/bin/python3
"""POST request to http://0.0.0.0:5000/search_user"""
if __name__ == '__main__':
    import requests
    import sys
    url = 'http://0.0.0.0:5000/search_user'
    letter = sys.argv[1] if len(sys.argv) > 1 else ''
    data = {'q': letter}
    request = requests.post(url, data)
    try:
        response = request.json()
        print('No result' if not response else
              '[{}] {}'.format(response.get('id'), response.get('name')))
    except ValueError:
        print("Not a valid JSON")
