#!/usr/bin/env python3 

"""
quicksort.py
This file holds the quicksort algorithm.
"""

__author__ = 'Theo Demetriades'
__version__ = '2021-03-15'

import time
import random
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

def median(array, i1, i2, i3):
    if (array[i1].getValue()<=array[i2].getValue() and array[i1].getValue()>=array[i3].getValue())\
         or (array[i1].getValue()<=array[i3].getValue() and array[i1].getValue()>=array[i2].getValue()):
        return i1
    elif (array[i2].getValue()<=array[i1].getValue() and array[i2].getValue()>=array[i3].getValue())\
         or (array[i2].getValue()<=array[i3].getValue() and array[i2].getValue()>=array[i1].getValue()):
        return i2
    else:
        return i3
    
swaps = 0

def quicksort(array, start, stop, w, LINE_WIDTH):
    if stop-start<1:
        return
    global swaps
    if stop-start==1:
        if array[start].getValue()<=array[stop].getValue():
            return
        else:
            array[start].setColor('red')
            array[stop].setColor('red')
            array[start], array[stop] = array[stop], array[start]
            array[start].theTurtle().goto(start*LINE_WIDTH, 0)
            array[stop].theTurtle().goto(stop*LINE_WIDTH, 0)
            array[start].setColor('white')
            array[stop].setColor('white')
            swaps+=1
            return

    pivot = array[stop].getValue()
        
    lefti = start
    righti = stop-1

    while lefti<righti:
        while array[lefti].getValue()<=pivot and lefti<=righti:
            lefti+=1
        while array[righti].getValue()>pivot and righti>lefti:
            righti-=1
        if lefti<righti:
            array[lefti].setColor('red')
            array[righti].setColor('red')
            array[lefti], array[righti] = array[righti], array[lefti]
            array[lefti].theTurtle().goto(lefti*LINE_WIDTH, 0)
            array[righti].theTurtle().goto(righti*LINE_WIDTH, 0)
            array[lefti].setColor('white')
            array[righti].setColor('white')
            swaps+=1
    if lefti==righti and array[righti].getValue()>pivot:
        array[righti].setColor('red')
        array[stop].setColor('red')
        array[righti], array[stop] = array[stop], array[righti]
        array[righti].theTurtle().goto(righti*LINE_WIDTH, 0)
        array[stop].theTurtle().goto(stop*LINE_WIDTH, 0)
        array[righti].setColor('white')
        array[stop].setColor('white')
        swaps+=1
    else:
        array[lefti].setColor('red')
        array[stop].setColor('red')        
        array[stop], array[lefti] = array[lefti], array[stop]
        array[lefti].theTurtle().goto(lefti*LINE_WIDTH, 0)
        array[stop].theTurtle().goto(stop*LINE_WIDTH, 0)
        array[lefti].setColor('white')
        array[stop].setColor('white')
        swaps+=1        

    quicksort(array, start, lefti-1, w, LINE_WIDTH)
    quicksort(array, lefti+1, stop, w, LINE_WIDTH)

def selectionsort(nums, w, LINE_WIDTH):
    """Takes the list "nums" and sorts it using the
    Selection Sort algorithm. Also moves those turtles to their
    new locations in the window.
    """
    for i in range(len(nums)):
        smallestLoc = i
        for j in range(i, len(nums)):
            if nums[j].getValue() < nums[smallestLoc].getValue():
                smallestLoc = j
        nums[i].setColor("red") # color the turtles we're swapping
        nums[smallestLoc].setColor("lime")
        nums[smallestLoc], nums[i] = nums[i], nums[smallestLoc] # swap
        # Now move the turtles
        nums[smallestLoc].theTurtle().goto(smallestLoc * LINE_WIDTH, 0)
        global swaps 
        swaps+=1
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
    
    for value in values:
        value.setColor('lime')
        
    w.exitonclick()
    
    global swaps

    print(f'Quicksort performed {str(swaps)} swaps to sort the array of {str(NUM_OF_VALUES)} integers.')
    



if __name__ == '__main__':
    main()
                

   
    