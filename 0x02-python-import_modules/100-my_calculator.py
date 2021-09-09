#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys
    args = sys.argv
    operators = {"+": add, "-": sub, "*": mul, "/": div}
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if args[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(args[1])
    operator = args[2]
    b = int(args[3])
    c = operators[args[2]](a, b)
    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, c))
