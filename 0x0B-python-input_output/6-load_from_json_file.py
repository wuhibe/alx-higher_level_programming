#!/usr/bin/python3
'''
Module that works with JSON files
'''

import json


def load_from_json_file(filename):
    ''' Create an object from JSON file '''
    with open(filename, 'r') as open_file:
        return json.load(open_file)
