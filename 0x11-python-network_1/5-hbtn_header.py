#!/usr/bin/python3
'''
send request to custom URL and display value of X-Request-Id
'''
import requests
from sys import argv
if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers.get('x-request-id'))
