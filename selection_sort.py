#!/usr/bin/env python3
"""
selection_sort.py
Creates a list of random values and sorts them using the 
Selection Sort algorithm.
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
    
    
def selection_sort(nums):
    """Takes the list "nums" and sorts it using the
    Selection Sort algorithm.
    """
    for i in range(len(nums)-1):
        small_index = i
        for x in range(i+1, len(nums)):
            if nums[x]<nums[small_index]:
                small_index = x
        if i != small_index:
            nums[small_index], nums[i] = nums[i], nums[small_index]
    return nums
            
    
        
def display(a_list):
    """Prints out the list "a_list" on the screen. To
    be used for debugging, or displaying the initial
    and final state of the list.
    """
    print(a_list)
    
    
    
def main():
    NUM_OF_VALUES = 10
    nums = generate_random_numbers(NUM_OF_VALUES, 10)
    display(nums)
    start = time.time()
    selection_sort(nums)
    stop = time.time()
    display(nums)
    print("Sorted {0:10d} values, execution time: {1:10.5f} seconds".format(NUM_OF_VALUES, stop - start))
    
if __name__ == "__main__":
    main()