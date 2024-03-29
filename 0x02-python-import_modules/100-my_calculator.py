#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    valid_operators = ['+', '*', '/', '-']

    if (len(sys.argv) - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op = sys.argv[2]
    if op in valid_operators:
        if op == '+':
            print("{} {} {} = {}".format(a, op, b, add(a, b)))
            sys.exit(0)
        elif op == '-':
            print("{} {} {} = {}".format(a, op, b, sub(a, b)))
            sys.exit(0)
        elif op == '*':
            print("{} {} {} = {}".format(a, op, b, mul(a, b)))
            sys.exit(0)
        elif op == '/':
            print("{} {} {} = {}".format(a, op, b, div(a, b)))
            sys.exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
