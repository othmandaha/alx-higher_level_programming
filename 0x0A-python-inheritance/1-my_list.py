#!/usr/bin/python3
""" A list class """


class Mylist(List):
    """ a child class of list """

    def __init__(self):
        """ initialize the child class """
        super().__init__()
        """ initialize the parent class"""

    def print_sorted(self):
        """ print sorted """
        print(sorted(self))
