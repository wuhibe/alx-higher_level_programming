#!/usr/bin/python3
'''
Module to append text to file
'''


def append_write(filename="", text=""):
    ''' Appends text to file '''
    with open(filename, 'a') as open_file:
        count = open_file.write(text)
    return count
