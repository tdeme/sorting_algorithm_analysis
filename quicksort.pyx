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

cdef void _quicksort(int array[], const int start, const int stop):
    if stop-start<1:
        return
    if stop-start==1:
        if array[start]<=array[stop]:
            return
        else:
            array[start], array[stop] = array[stop], array[start]
            return

    cdef int pivot = array[stop]
    cdef int lefti = start
    cdef int righti = stop-1

    while lefti<righti:
        while array[lefti]<=pivot and lefti<=righti:
            lefti+=1
        while array[righti]>pivot and righti>lefti:
            righti-=1
        if lefti<righti:
            array[lefti], array[righti] = array[righti], array[lefti]
    if lefti==righti and array[righti]>pivot:
        array[righti], array[stop] = array[stop], array[righti]
    else:
        array[stop], array[lefti] = array[lefti], array[stop]

    _quicksort(array, start, lefti-1)
    _quicksort(array, lefti+1, stop)

def quicksort(array, first, last):
    cdef int arr[100000]
    cdef int start = first
    cdef int stop = last
    for i in range(stop-start):
        arr[start+i]=array[start+i]
    _quicksort(arr, start, stop)


    '''if len(array)<=1 or (len(array)==2 and array[0]<=array[1]):
    return array

    pivot = array.pop(len(array)//2)
    lows = []
    highs = []
    for num in array:
        if num>pivot:
            highs.append(num)
        else:
            lows.append(num)
    
    return quicksort(lows) + [pivot] + quicksort(highs)'''

def main():
    array = generate_random_numbers(100, 100)
    print(array)
    start = time.time()
    quicksort(array, 0, 99)
    print(f'Time: {str(time.time()-start)}')
    print(array)


if __name__ == '__main__':
    main()
                

   
    