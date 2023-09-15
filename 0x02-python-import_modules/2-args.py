#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numb = len(sys.argv) - 1
    if numb == 0:
        print("0 arguments.")
    elif numb == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(numb))
    for i in range(numb):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
