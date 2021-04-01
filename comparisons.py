#!/usr/bin/env python 3

"""
comparisons.py
This program times, compares, and graphs the performance
of selection_sort(), insertion_sort(), and quicksort().
"""

__author__ = 'Theo Demetriades'
__version__ = '2021-03-18'

from selection_sort import *
from insertion_sort import insertion_sort
from counting_sort import counting_sort
from quicksort import quicksort
import matplotlib.pyplot as plt

def runTests(n):
    """This function times each sorting algorithm for different
    list sizes n, and returns lists filled with the sizes and times
    for each algorithm."""

    sizes = []
    selection_times = []
    insertion_times = []
    counting_times = []
    quick_times = []

    for i in range(1, n, n//10):
        sizes.append(i)

        arr = generate_random_numbers(i, i)
        selection_start = time.time()
        selected = selection_sort(arr)
        selection_time = time.time()-selection_start
        selection_times.append(selection_time)

        arr = generate_random_numbers(i, i)
        insertion_start = time.time()
        inserted = insertion_sort(arr)
        insertion_time = time.time()-insertion_start
        insertion_times.append(insertion_time)

        arr = generate_random_numbers(i, i)
        counting_start = time.time()
        counted = counting_sort(arr)
        counting_time = time.time()-counting_start
        counting_times.append(counting_time)

        arr = generate_random_numbers(i, i)
        quickstart = time.time()
        quicksort(arr,0,i-1)
        quick_time = time.time()-quickstart
        quick_times.append(quick_time)

    return sizes, selection_times, insertion_times, counting_times, quick_times

def graphResults(sizes, selection_times, insertion_times, counting_times, quick_times):
    plt.plot(sizes, selection_times)
    plt.suptitle('Selection Sort')
    plt.xlabel('Number of Values')
    plt.ylabel('Time to Sort (Seconds)')
    plt.show()

    plt.plot(sizes, insertion_times)
    plt.suptitle('Insertion Sort')
    plt.xlabel('Number of Values')
    plt.ylabel('Time to Sort (Seconds)')
    plt.show()

    plt.plot(sizes, counting_times)
    plt.suptitle('"Counting" Sort')
    plt.xlabel('Number of Values')
    plt.ylabel('Time to Sort (Seconds)')
    plt.show()

    plt.plot(sizes, quick_times)
    plt.suptitle('Quick Sort')
    plt.xlabel('Number of Values')
    plt.ylabel('Time to Sort (Seconds)')
    plt.show()


def main():
    sizes, selection_times, insertion_times, counting_times, quick_times \
    = runTests(10000)

    print(f'Selection times: {str(selection_times)}')
    print(f'Insertion times: {str(insertion_times)}')
    print(f'Counting times: {str(counting_times)}')
    print(f'Quick times: {str(quick_times)}')

    graphResults(sizes, selection_times, insertion_times, counting_times, quick_times)


if __name__=='__main__':
    main()





