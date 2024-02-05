#!/usr/bin/python3
""" A list class """


class MyList(list):
    """ a child class of list """

    def print_sorted(self):
        """ print sorted """
        print(sorted(self))
