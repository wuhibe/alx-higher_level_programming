#!/usr/bin/python3
'''
displays the value of the X-Request-Id variable
'''
if __name__ == '__main__':
    import sys
    import urllib.request
    with urllib.request.urlopen(sys.argv[1]) as res:
        print(res.info()['X-Request-Id'])
