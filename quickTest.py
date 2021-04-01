#!/usr/bin/env python3

from quicksort import *

def main():
    array = generate_random_numbers(100, 100)
    print(array)
    start = time.time()
    quicksort(array, 0, 99)
    finished = time.time()-start
    print(finished)

main()