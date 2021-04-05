#!/usr/bin/env python3

from quicksort import *
import numpy as np

def main():
    array = np.array(generate_random_numbers(8500000, 8500000))
    start = time.time()
    result = quicksort(array, 0, 8499999)
    print(f'Quick time for 8500000 integers: {str(time.time()-start)}')
    print(array[:10])

    array2 = np.array(generate_random_numbers(8500000, 8500000))
    start2 = time.time()
    array2.sort()
    print(f'Built-in time for 8500000 integers: {str(time.time()-start2)}')
    print(array2[:10])

if __name__ == '__main__':
    main()
              