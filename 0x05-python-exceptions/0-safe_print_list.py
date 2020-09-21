#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elem = 0

    try:
        for elem in range(x):
            print("{}".format(my_list[elem]), end="")
            elem += 1
    except IndexError:
        pass
    print()
    return elem
