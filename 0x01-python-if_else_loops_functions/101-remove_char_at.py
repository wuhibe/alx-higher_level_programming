#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n > len(str):
        return str
    str2 = ""
    for i in str:
        if str[n] == i:
            continue
        else:
            str2 = str2 + i
    return str2
