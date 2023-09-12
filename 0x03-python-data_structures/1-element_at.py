#!/usr/bin/python3
def element_at(my_list, idx):
    B = len(my_list) - 1
    for idx in range(B):
        if idx > 0:
            return None
        elif idx > B:
            return None
        return (my_list[idx])
