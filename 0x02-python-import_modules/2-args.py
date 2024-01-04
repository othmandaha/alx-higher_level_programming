#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    length = len(sys.argv) - 1
    if length == 1:
        print("{} argument:".format(length))
    elif length == 0:
        print("{} arguments.".format(lenght))
    else:
        print("{} arguments:".format(length))

    i = 1
    while i <= length:
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
