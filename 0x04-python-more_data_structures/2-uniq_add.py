#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq = set(my_list)
    Sum = 0
    for x in uniq:
        Sum += x

    return Sum
