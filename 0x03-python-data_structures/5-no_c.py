#!/usr/bin/python3
def no_c(my_string):
    b = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        else:
            b = b + i
    return b
