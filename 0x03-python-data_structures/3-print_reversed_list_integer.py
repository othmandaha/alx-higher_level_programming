#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        while len(my_list) != 0:
            print("{:d}".format(my_list.pop()))
