#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) < 1:
        print("{}".format(0))
    else:
        j = 1
        i = 0
        while j != len(argv):
            i += int(argv[j])
            j += 1
        print("{}".format(i))
