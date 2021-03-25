#!/usr/bin/env python3 

"""
counting_sort.py
This file holds a counting sort algorithm which uses
a dictionary to hold the occurances of each integer in 
the random list.
"""

__author__ = 'Theo Demetriades'
__version__ = '2021-04-09'

import random
import time

def counting_sort(l):
    new = []
    occurances = {}
    for integer in l:
        if integer in occurances.keys():
            occurances[integer]+=1
        else:
            occurances[integer] = 1
    for i in range(len(l)):
        if i in occurances.keys():
            for x in range(occurances[i]):
                new.append(i)
    return new

def main():
    list = []
    for i in range(100):
        list.append(random.randrange(100))
    print(list)
    print(counting_sort(list))


if __name__=='__main__':
    main()