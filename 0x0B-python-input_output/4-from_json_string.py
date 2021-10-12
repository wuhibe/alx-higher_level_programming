#!/usr/bin/python3
import json
'''
Module that works with JSON
'''


def from_json_string(my_str):
    ''' Returns an object from JSON string '''
    return json.loads(my_str)
