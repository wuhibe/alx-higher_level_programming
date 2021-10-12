#!/usr/bin/python3
'''
Module that adds args to JSON file
'''

import sys
import os

arg_list = sys.argv[1:]

save_JSON = __import__('5-save_to_json_file').save_to_json_file
load_JSON = __import__('6-load_from_json_file').load_from_json_file

lisst = []
if os.path.exists('add_item.json'):
    lisst = load_JSON('add_item.json')

save_JSON(lisst + arg_list, "add_item.json")
