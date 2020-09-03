#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    argc = len(argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operation = {"+": add, "-": sub, "*": mul, "/": div}
    operator = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    if operator in list(operation.keys()):
        print("{} {} {} = {}".format(a, operator, b,
                                     operation[operator](a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
