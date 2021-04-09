#!/usr/bin/env python3 

"""
quicksort.py
This file holds the quicksort algorithm.
"""

__author__ = 'Theo Demetriades'
__version__ = '2021-03-15'

import time
import random
import os
from turtle import *

class Value(object):
    def __init__(self, val):
        self.val = val
        self.t = Turtle()
        self.t.speed(0)
        self.t.penup()
        self.t.color('white')
        self.t.hideturtle()
        self.t.shape('square')

    def setTurtleSize(self, height, width):
        self.t.turtlesize(((self.val+1)*height), width, 0)

    def getValue(self):
        return self.val
    
    def theTurtle(self):
        return self.t

    def setColor(self, newColor):
        self.t.color(newColor)

    def __repr__(self):
        return f'Turtle[value={str(self.val)}, theTurtle={str(self.t)}'

def init_screen(n):
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 800
    w = Screen()
    w.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
    w.screensize(WINDOW_WIDTH, WINDOW_HEIGHT)
    w.setworldcoordinates(0, 0, w.window_width(), w.window_height())
    w.bgcolor('black')
    LINE_WIDTH = w.window_width() / (n)

    values = []
    for i in range(n):
        new_value = Value(i*(WINDOW_HEIGHT/n))
        new_value.setTurtleSize(WINDOW_HEIGHT/9000, 0.1)
        values.append(new_value)
    random.shuffle(values)
    display_turtles(values, w, LINE_WIDTH)
    return values, w, LINE_WIDTH

def display_turtles(values, w, LINE_WIDTH):
    for i in range(len(values)):
        values[i].theTurtle().goto(i*LINE_WIDTH, 0)
        values[i].theTurtle().showturtle()

def generate_random_numbers(length, range_of_values):
    """Generates a list of "length" integers randomly
    selected from the range 0 (inclusive) to 
    range_of_values (exclusive) and returns it to 
    the caller.
    """
    return [random.randrange(range_of_values) for i in range(length)]


def swap_turtles(array, t1, t2, LINE_WIDTH):
    array[t1].setColor('red')
    array[t2].setColor('red')
    array[t1], array[t2] = array[t2], array[t1]
    array[t1].theTurtle().goto(t1*LINE_WIDTH, 0)
    array[t2].theTurtle().goto(t2*LINE_WIDTH, 0)
    array[t1].setColor('white')
    array[t2].setColor('white')

def refresh():
    os.system('clear')
    print(f'Comparisons: {str(comparisons)} \nSwaps: {str(swaps)}')
    
swaps = 0
comparisons = 0

def quicksort(array, start, stop, w, LINE_WIDTH):
    global comparisons
    comparisons+=1
    refresh()
    if stop-start<1:
        return
    global swaps
    comparisons+=1
    refresh()
    if stop-start==1:
        comparisons+=1
        refresh()
        if array[start].getValue()<=array[stop].getValue():
            return
        else:
            swap_turtles(array, start, stop, LINE_WIDTH)
            swaps+=1
            refresh()
            return

    pivot = array[stop].getValue()
        
    lefti = start
    righti = stop-1

    while lefti<righti:
        comparisons+=2
        refresh()
        while array[lefti].getValue()<=pivot and lefti<=righti:
            lefti+=1
        comparisons+=2
        refresh()
        while array[righti].getValue()>pivot and righti>lefti:
            righti-=1
        comparisons+=1
        refresh()
        if lefti<righti:
            swap_turtles(array, lefti, righti, LINE_WIDTH)
            swaps+=1
            refresh()
        comparisons+=1
        refresh()
    else:
        swap_turtles(array, lefti, stop, LINE_WIDTH)
        swaps+=1   
        refresh()     

    quicksort(array, start, lefti-1, w, LINE_WIDTH)
    quicksort(array, lefti+1, stop, w, LINE_WIDTH)

def selectionsort(nums, w, LINE_WIDTH):
    """Takes the list "nums" and sorts it using the
    Selection Sort algorithm. Also moves those turtles to their
    new locations in the window.
    """
    global comparisons
    global swaps
    for i in range(len(nums)):
        smallestLoc = i
        for j in range(i, len(nums)):
            comparisons+=1
            refresh()
            if nums[j].getValue() < nums[smallestLoc].getValue():
                smallestLoc = j
        nums[i].setColor("red") # color the turtles we're swapping
        nums[smallestLoc].setColor("lime")
        nums[smallestLoc], nums[i] = nums[i], nums[smallestLoc] # swap
        # Now move the turtles
        nums[smallestLoc].theTurtle().goto(smallestLoc * LINE_WIDTH, 0)
        swaps+=1
        refresh()
        if i != smallestLoc:
            nums[smallestLoc].setColor("white")
        nums[i].theTurtle().goto(i * LINE_WIDTH, 0)


def main():
    print('Graphical presentation of QuickSort using turtle module.')
    input('Press [Enter] to continue...')

    NUM_OF_VALUES = 100
    print(f'Please be patient while {str(NUM_OF_VALUES)} turtles are created...')
    values, w, LINE_WIDTH = init_screen(NUM_OF_VALUES)

    quicksort(values, 0, 99, w, LINE_WIDTH)
    refresh()

    #selectionsort(values, w, LINE_WIDTH)
    #refresh()
    
    values = [value.setColor('lime') for value in values]
        
    w.exitonclick()
    
    global swaps
    global comparisons

    print(f'Quicksort performed {str(comparisons)} comparisons and'\
        f' {str(swaps)} swaps to sort the array of {str(NUM_OF_VALUES)} integers.')


if __name__ == '__main__':
    main()
                

   
    