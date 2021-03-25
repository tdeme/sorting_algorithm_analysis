#!/usr/bin/env python3
"""
insertion_sort.py
Creates a list of random values and sorts them using the 
Insertion Sort algorithm.
@author 
@version 
"""

import time
import random

def generate_random_numbers(length, range_of_values):
    """Generates a list of "length" integers randomly
    selected from the range 0 (inclusive) to 
    range_of_values (exclusive) and returns it to 
    the caller.
    """
    return [random.randrange(range_of_values) for i in range(length)]
    
    
def insertion_sort(nums):
    """Takes the list "nums" and sorts it using the
    Insertion Sort algorithm.
    """
    for i in range(1, len(nums)):
        index = i
        while nums[index]<nums[index-1] and index>0:
            nums[index-1], nums[index] = nums[index], nums[index-1]
            index-=1

    return nums
            
        
def display(a_list):
    """Prints out the list "a_list" on the screen. To
    be used for debugging, or displaying the initial
    and final state of the list.
    """
    print(a_list)
    
    
    
def main():
    NUM_OF_VALUES = 100
    nums = generate_random_numbers(NUM_OF_VALUES, 1000)
    display(nums)
    start = time.time()
    insertion_sort(nums)
    stop = time.time()
    display(nums)
    print("Sorted {0:10d} values, execution time: {1:10.5f} seconds".format(NUM_OF_VALUES, stop - start))
    
if __name__ == "__main__":
    main()