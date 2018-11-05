#!/usr/bin/env python3

import operator
import readline
import colored
from colored import fg, bg, attr, fore, back, style

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '%': operator.mod,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError('%s%s Too many parameters %s' % (fg(1), bg(15), attr(0)))
    return stack.pop()

def main():
    while True:
        result = calculate(input(fore.YELLOW + style.BOLD + "rpn calc> " + style.RESET))
        print('%s%sResult: %s' % (fg('orchid'), attr('bold'), attr('reset')), result)

if __name__ == '__main__':
    main()
