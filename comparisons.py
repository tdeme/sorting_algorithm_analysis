#!/usr/bin/env python 3

"""
comparisons.py
This program times, compares, and graphs the performance
of selection_sort(), insertion_sort(), and quicksort().
"""

__author__ = 'Theo Demetriades'
__version__ = '2021-03-18'

from counting_sort import counting_sort
from quicksort import *
import matplotlib.pyplot as plt
import numpy as np

def runTests(n):
    """This function times each sorting algorithm for different
    list sizes n, and returns lists filled with the sizes and times
    for each algorithm."""

    sizes = []
    selection_times = []
    insertion_times = []
    counting_times = []
    quick_times = []
    tim_times = []

    for i in range(1, n+1, n//20):
        sizes.append(i)

        arr = np.array(generate_random_numbers(i, i))
        counting_start = time.time()
        counted = counting_sort(arr)
        counting_time = time.time()-counting_start
        counting_times.append(counting_time)

        arr = np.array(generate_random_numbers(i, i))
        quickstart = time.time()
        quicksort(arr,0,i-1)
        quick_time = time.time()-quickstart
        quick_times.append(quick_time)

        arr = np.array(generate_random_numbers(i, i))
        timstart = time.time()
        arr.sort()
        tim_time = time.time()-timstart
        tim_times.append(tim_time)

    return sizes, counting_times, quick_times, tim_times

def graphResults(sizes, counting_times, quick_times, tim_times):

    plt.plot(sizes, counting_times, label = '"Counting" Sort')
    plt.plot(sizes, quick_times, label = 'Quicksort')
    plt.plot(sizes, tim_times, label = 'Built-In sort()')
    plt.suptitle('Number of Values vs. Time')
    plt.xlabel('Number of Values')
    plt.ylabel('Time to Sort (Seconds)')
    plt.legend()
    plt.show()

def main():
    sizes, counting_times, quick_times, tim_times = runTests(100000)

    print(f'Counting times: {str(counting_times)}')
    print(f'Quick times: {str(quick_times)}')
    print(f'Tim times: {str(tim_times)}')

    graphResults(sizes, counting_times, quick_times, tim_times)


if __name__=='__main__':
    main()





