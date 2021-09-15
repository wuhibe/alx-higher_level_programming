#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        average = 0
        denom = 0
        summ = 0
        for i in my_list:
            denom += i[1]
            summ += i[0] * i[1]
        return summ/denom
    else:
        return 0
