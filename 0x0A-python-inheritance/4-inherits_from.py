#!/usr/bin/python3
'''if the object is an instance of a class that inherited
(directly or indirectly) from the specified class'''


def inherits_from(obj, a_class):
    '''traitement'''

    if isinstance(obj, a_class) and not type(obj) is a_class:
        return True
    return False
