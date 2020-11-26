# -*- coding: utf-8 -*-

str = 'abcdefg'

print(str[2])
print(str[-1:])


def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument')


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
