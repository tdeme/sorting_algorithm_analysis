#!/usr/bin/env python3
"""
selectionsort.py
This program uses a Value class to associate a value in an array and a
Turtle object that will represent that value graphically.
This version works relatively quickly, once the Turtle objects have all been
created. There are some issues with the dimensions of the screen and the bars--
it's all a bit hacked together, there--but the basic functioning of the program
is fine, and 1000 values can be displayed and sorted within a minute or so.
@author Richard White
@version 2017-03-24
"""
import random
from turtle import *
#############################
class Value():
    """Defines a Value in terms of its magnitude, and maintains
    a turtle object for displaying a graphical form of that value.
    """
    def __init__(self, value):
        self.value = value
        self.t = Turtle()
        self.t.speed(0) # 0 = fastest speed possible
        self.t.penup() # don’t draw turtle path
        self.t.color("black") # turtle will be black on white bg
        self.t.hideturtle() # don’t show turtle (yet)
        self.t.shape("square") # actually a rectangle
    def setTurtleSize(self, height, width):
        self.t.turtlesize(((self.value + 1) * height), width, 0)

    def getValue(self):
        return self.value

    def theTurtle(self):
        return self.t
    def setColor(self, newColor):
        self.t.color(newColor)

    def __str__(self):
        return "Turtle[value=" + str(self.value) + ",theTurtle=" + str(self.t)
#############################
def initialize(n):
 """Sets up the screen, and creates an array of n Value objects
 in a list arr, where each value has a turtle associated with it.
 """
 WINDOW_WIDTH = 1200
 WINDOW_HEIGHT = 800
 w = Screen()
 w.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
 w.screensize(WINDOW_WIDTH, WINDOW_HEIGHT)
 w.setworldcoordinates(0,0,w.window_width(), w.window_height())
 w.bgcolor("white")
 LINE_WIDTH = w.window_width() / (n) # Identify line width based
 # on number of turtles and
 # screen width
 arr = []
 for i in range(n):
    randNum = int(random.random() * WINDOW_HEIGHT + 1)
    new_value = Value(randNum)
    '''
    TurtleSize parameter calculations include "magic number" 9000
    and 0.1, determined through experimentation with Turtle graphics
    May need to be adjusted for other monitors, window sizes, etc.
    '''
    new_value.setTurtleSize(WINDOW_HEIGHT / 9000, 0.1)
    arr.append(new_value)
    display_turtles(arr, w, LINE_WIDTH)
 return arr, w, LINE_WIDTH
#############################
def display_turtles(arr, w, LINE_WIDTH):
    """Goes through the array of turtles, and puts each
    turtle at the appropriate location on the screen,
    then shows it.
    """
    for i in range(len(arr)):
        arr[i].theTurtle().goto(i * LINE_WIDTH, 0)
        arr[i].theTurtle().showturtle()

#############################
def generate_random_numbers(length, range_of_values):
    """Generates a list of "length" integers randomly
    selected from the range 0 (inclusive) to
    range_of_values (exclusive) and returns it to
    the caller.
    """
    nums = []
    for i in range(length):
        nums.append(random.randrange(range_of_values))
    return nums
#############################
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
    nums[smallestLoc].setColor("green")
    nums[smallestLoc], nums[i] = nums[i], nums[smallestLoc] # swap
    # Now move the turtles
    nums[smallestLoc].theTurtle().goto(smallestLoc * LINE_WIDTH, 0)
    if i != smallestLoc:
        nums[smallestLoc].setColor("black")
    nums[i].theTurtle().goto(i * LINE_WIDTH, 0)

#############################
def main():
    print("Graphical presentation of SelectionSort using turtle module")
    input("Press [Enter] to continue...")
    NUM_OF_VALUES = 300
    print("Please be patient while",NUM_OF_VALUES,"turtles are created...")
    arr, w, LINE_WIDTH = initialize(NUM_OF_VALUES)
    selectionsort(arr, w, LINE_WIDTH) # perform sort
    w.exitonclick() # leave image on screen

if __name__ == "__main__":
 main()