#!/usr/bin/python3
'''
script that fetches https://intranet.hbtn.io/status
'''
import urllib.request as req

if __name__ == '__main__':
    with req.urlopen('https://intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
