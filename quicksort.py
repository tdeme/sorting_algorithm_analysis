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
    lows = []
    highs = []
    for num in array:
        if num>pivot:
            highs.append(num)
        else:
            lows.append(num)
    
    return quicksort(lows) + [pivot] + quicksort(highs)

def main():
    array = generate_random_numbers(100, 100)
    print(array)
    start = time.time()
    print(quicksort(array))
    print(f'Time: {str(time.time()-start)}')


if __name__ == '__main__':
    main()
                

   
    