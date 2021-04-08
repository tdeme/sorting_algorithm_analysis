#!/usr/bin/env python3

from quicksort import *
import numpy as np

def main():
    times = []
    for _ in range(10):
        array = np.array(generate_random_numbers(1000000, 1000000))
        start = time.time()
        quicksort(array, 0, 999999)
        finished = time.time()
        times.append(finished-start)
    print(times)
    print(f'Average time: {sum(times)/len(times)}')
if __name__ == '__main__':
    main()
              