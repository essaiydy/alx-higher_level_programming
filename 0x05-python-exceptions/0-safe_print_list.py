#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range (x):
            for j in range (i):
          print("{}".format(my_list[i]), end="")
                  j++
    except IndexError:
    return(j)
