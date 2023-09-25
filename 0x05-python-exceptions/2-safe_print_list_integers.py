#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    #    try:
    j = 0
    for i in range(x):
        if type(my_list[i]) is int:
            print("{:d}".format(my_list[i]), end="")
            j = j + 1
        continue
    print("")
#    except:
    return j
