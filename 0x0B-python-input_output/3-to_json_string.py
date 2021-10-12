#!/usr/bin/python3
import json
'''
Module to work with JSON
'''


def to_json_string(my_obj):
    ''' Returns JSON representation of an object '''
    return str(json.dumps(my_obj))
