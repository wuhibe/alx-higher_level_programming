#!/usr/bin/python3
'''
Module to work on files with JSON
'''

import json


def save_to_json_file(my_obj, filename):
    ''' Prints JSON representation of object to file '''
    with open(filename, 'w') as open_file:
        open_file.write(json.dumps(my_obj))
