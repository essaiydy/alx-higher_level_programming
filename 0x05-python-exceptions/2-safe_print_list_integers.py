#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        j = 0
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            j = j + 1
        print("")
    except (TypeError, ValueError, IndexError):
        print("") 
    return j
