#!/usr/bin/python3
'''
use the GitHub API to display your id
'''
import requests
from sys import argv
if __name__ == "__main__":
    response = requests.get('https://api.github.com/user',
                            auth=(argv[1], argv[2]))
    if "json" not in response.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        response = response.json()
        print(response.get('id'))
