#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except ValueError:
        '''print("{} is not an integer".format(value))'''
        return (False)
    return (True)