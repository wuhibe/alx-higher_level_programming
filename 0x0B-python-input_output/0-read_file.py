#!/usr/bin/python3
'''
Module to read and print contents of a file
'''


def read_file(filename=""):
    ''' Reads file and prints contents '''
    with open(filename) as open_file:
        contents = open_file.read()
    print(contents, end="")
