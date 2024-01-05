#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    tuple_aa = tuple_a + (0, 0)
    tuple_bb = tuple_b + (0, 0)
    new_tuple = (tuple_aa[0] + tuple_bb[0], tuple_aa[1] + tuple_bb[1])
    return new_tuple
