#!/usr/bin/env python3

from quicksort import *
import numpy as np

def main():
    array = np.array(generate_random_numbers(1000000, 1000000))
    start = time.time()
    quicksort(array, 0, 999999)
    print(f'Time: {str(time.time()-start)}')
    print(array[:10])

if __name__ == '__main__':
    main()
              