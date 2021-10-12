#!/usr/bin/python3
import json
'''
Module to work on files with JSON
'''


def save_to_json_file(my_obj, filename):
    ''' Prints JSON representation of object to file '''
    with open(filename, 'w') as open_file:
        json.dump(my_obj, open_file)
