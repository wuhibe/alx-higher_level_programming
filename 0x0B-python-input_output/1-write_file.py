#!/usr/bin/python3
'''
Module to write to file
'''


def write_file(filename="", text=""):
    ''' Writes text to file '''
    with open(filename, 'w') as open_file:
        open_file.write(text)
        count = open_file.tell()
    return count
