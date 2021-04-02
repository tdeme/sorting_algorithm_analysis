#!/usr/bin/env python3 

from quicksort import *

def main():
    array = generate_random_numbers(1000000, 1000000)
    start = time.time()
    quicksort(array, 0, 999999)
    print(f'Time: {str(time.time()-start)}')
    print(array[:10])

main()
