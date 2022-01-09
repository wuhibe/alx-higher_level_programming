#!/usr/bin/python3
'''
module to find peak
'''


def find_peak(listint):
    ''' Function that returns peak value in a list '''
    if listint:
        m = listint[0]
        for i in listint:
            if i > m:
                m = i
        return m
    else:
        return None
