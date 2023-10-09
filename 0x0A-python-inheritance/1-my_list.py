#!/usr/bin/python3
'''a class MyList that inherits from list'''

class MyList(list):
    '''the sorted list'''

    def print_sorted(self):
        '''tje output'''

        return sorted(self)
