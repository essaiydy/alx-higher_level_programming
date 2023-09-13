#!/usr/bin/python3

def uniq_add(my_list=[]):
    somme = 0
    for i in set(my_list):
        somme += i
    return somme
