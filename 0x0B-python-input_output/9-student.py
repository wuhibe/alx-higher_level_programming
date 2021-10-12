#!/usr/bin/python3
'''
Module for class Student.
'''


class Student:
    ''' Student class '''

    def __init__(self, first_name, last_name, age):
        ''' Initialize class '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        ''' Return Dictionary to JSON '''
        return self.__dict__
