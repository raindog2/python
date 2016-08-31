#!/usr/bin/env python

# Copyright (C) 2014 Mark Purcell <mpurcell@uw.edu>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License,version 3
# as published by the Free Software Foundation.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# If you did not receive a copy of the GNU General Public License
# along with this program, see <http://www.gnu.org/licenses/>.

import os
os.system('clear')

from turtle import *

# Some basic turtle actions

# Function to draw a box
def box():
    pendown()
    for i in range(4):
        forward(100)
        left(90)
 
# Function to iterate the box all the way around a circle
def iterate_box():
    for i in range(36):
        box()
        left(10)

iterate_box()

# Move turtle to new location
left(45)
penup()
forward(300)

# Function to draw a triangle
def triangle():
    pendown()
    for i in range(3):
        forward(75)
        right(120)

# Function to iterate the triagle around in a circle
def iterate_triangle():
    for i in range(36):
        triangle()
        left(10)

iterate_triangle()

# Move turtle to new location
penup()
left(135)
forward(424)
right(45)

iterate_triangle()

# Exit after user click
exitonclick()

#def centipede(length, step, life):
#    penup()
#    theta = 0
#    dtheta = 1
#    for i in range(life):
#        forward(step)
#        left(theta)
#        theta += dtheta
#        stamp()
#        if i > length:
#            clearstamps(1)
#        if theta > 10 or theta < -10:
#            dtheta = -dtheta
#        if ycor() > 350:
#            left(30)

#def main():
#    setworldcoordinates(-400, -400, 400, 400)
#    centipede(14, 10, 400)
#    exitonclick()

#main()

