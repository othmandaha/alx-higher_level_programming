#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    length = len(argv) - 1
    print("{} arguments:".format(length))
    i = 1

    while i <= length:
        print("{}: {}".format(i, argv[i]))
        i += 1
