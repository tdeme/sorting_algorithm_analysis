from counting_sort import counting_sort
import matplotlib.pyplot as plt
import time
import random

def runTests():
    times = []
    sizes = []
    for size in range(0, 1000000, 10000):
        sizes.append(size)
        list = []
        for i in range(size):
            list.append(random.randrange(size))
        start = time.time()
        new = counting_sort(list)
        finished = time.time()-start
        times.append(finished)
    return sizes, times

def display_results(sizes, times):
    plt.plot(sizes, times)
    plt.suptitle('"Counting" Sort')
    plt.xlabel('Number of Values')
    plt.ylabel('Time to Sort (Seconds)')
    plt.show()

def main():
    sizes, times = runTests()
    display_results(sizes, times)



if __name__=='__main__':
    main()