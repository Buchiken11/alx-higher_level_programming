#!/usr/bin/python3
import sys
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    operators = {'+': add, '-': sub, '*': mul, '/': div}
    number_arg = len(sys.argv)
    if number_arg != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
        a = int(sys.argv[1])
        operators = sys.argv[2]
        b = int(sys.argv[3])
        if operators == '+':
            result = add(a, b)
        elif operators == '-':
            result = sub(a, b)
        elif operators == '*':
            result = mul(a, b)
        elif operators == '/':
            result = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
            print("{} {} {} = {}".format(a, operator, b, result))
