#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argc = len(argv) - 1
    if not argc:
        print("0 arguments.")
    else:
        print("{} arguments{}:" .format(argc, "s" if argc > 1 else ""))
    for i, x in enumerate(argv[1:], 1):
        print("{}: {}.".format(i, x))
