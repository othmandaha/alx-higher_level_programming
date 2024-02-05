#!/usr/bin/python3
""" a base geometry BluePrint """


class BaseGeometry:
    """ the Base geometry class """

    def area(self):
        """ are calculator """
        raise Exception("area() is not implemented")
