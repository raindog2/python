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

from math import pi

import os
os.system('clear')

def area(x):
    return pi * x ** 2

def circumference(x):
    return pi * (2 * x)
    
def sphere_surface(x):
    return 4 * pi * x ** 2

def sphere_volume(x):
    return 4 / 3 * pi * x ** 3

#def big_circle(x):
#   return area(x)

def annulus(x, y):
    return area(x) - area(y)
#    return pi * (x ** 2 - y ** 2)

def shell_volume(x, y):
    return sphere_volume(x) - sphere_volume(y)
            
def main():
    print("Welcome to the python circle and sphere figure-outer!\n")
    r = float(input("What is the radius of the circle/sphere you'd like to examine, in inches? "))
    print("\nThe area of the circle with radius", r, "is", area(r), "inches squared!\n")
    print("The circumference of the circle with radius", r, "is", circumference(r), "inches!\n")
    print("The surface area of the sphere with radius", r, "is", sphere_surface(r), "inches squared!\n")
    print("The volume of the sphere with radius", r, "is", sphere_volume(r), "inches cubed!\n")
    print("OK, but that was easy.  Let's do an annulus...")
    inner_r = float(input("What is the inner radius of the annulus? "))
    outer_r = float(input("What is the outer radius of the annulus? "))
    print("The area of your annulus is", annulus(outer_r, inner_r), "inches squared!\n")
    print("https://en.wikipedia.org/wiki/Annulus_(mathematics)\n")
    print("Still, easy.  What about a spherical shell?\n")
    inner_r_shell = float(input("What is the inner radius of the shell? "))
    outer_r_shell = float(input("What is the outer radius of the shell? "))
    print("HooHaa! The area of your spherical shell is", shell_volume(outer_r_shell, inner_r_shell), "inches cubed!")
    
#print("The area of the circle with radius", r, "is", area, "square inches!")

main()
