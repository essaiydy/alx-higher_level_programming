#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    var = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > var:
            var = my_list[i]

    return (var)
