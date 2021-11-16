#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("{:d} arguments:".format(len(sys.argv) - 1))
    else:
        print("{:d} argument:".format(len(sys.argv) - 1))
    for i in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(i, sys.argv[i]))
