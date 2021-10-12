#!/usr/bin/python3
'''
Module to work with JSON
'''

import json


def to_json_string(my_obj):
    ''' Returns JSON representation of an object '''
    return json.dumps(my_obj)
