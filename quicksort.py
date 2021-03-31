#!/usr/bin/env python3 

"""
quicksort.py
This file holds the quicksort algorithm.
"""

__author__ = 'Theo Demetriades'
__version__ = '2021-03-15'

import time
import random

def generate_random_numbers(length, range_of_values):
    """Generates a list of "length" integers randomly
    selected from the range 0 (inclusive) to 
    range_of_values (exclusive) and returns it to 
    the caller.
    """
    return [random.randrange(range_of_values) for i in range(length)]

def quicksort(array):
    if len(array)<=1 or (len(array)==2 and array[0]<=array[1]):
        return array

    pivot = array.pop(len(array)//2)
    array.append(pivot)

    lefti = 0
    righti = len(array)-2
    while lefti<righti:
        while array[lefti]<=pivot and lefti<len(array)-2:
            lefti+=1
        while array[righti]>pivot and righti>=0:
            righti-=1
        if lefti<righti:
            array[lefti], array[righti] = array[righti], array[lefti]
    if array[lefti]<pivot:
        array[lefti-1], array[lefti] = array[lefti], array[lefti-1]
    else:
        array[lefti], array[-1] = array[-1], array[lefti]

    return quicksort(array[:lefti])+[pivot]+quicksort(array[lefti+1:])

def main():
    array = generate_random_numbers(100, 100)
    print(array)
    start = time.time()
    print(quicksort(array))
    print(f'Time: {str(time.time()-start)}')


if __name__ == '__main__':
    main()
                

   
    