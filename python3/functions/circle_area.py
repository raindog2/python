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

# This program is written for Python3.2

from math import pi
import time
import os
os.system('clear')

print('Hello, welcome to the python "perfect circle"!\n')

r = input("What is the radius (in inches) of the circle you want to find the area of? ")
r = float(r)
area = pi * r ** 2
print("\nThe area of a circle with radius", r, "is", area, "square inches!")

time.sleep(3)

input("\nOK, let's do the circumference of a circle with that radius...ready? ")
D = 2 * r
circumference = pi * D 
print("\nThe circumference of a circle with radius", r, "inches is", circumference, "inches!")

time.sleep(3)

input("\nWhile we are at it, we might as well do the surface area of a sphere with that same radius, right? ")
surf_sphere = 4 * pi * r ** 2
print("\nThe surface area of a sphere with radius", r, "is", surf_sphere, "square inches!!")

time.sleep(3)

input("\nOK, final thing: let's do the volume of the sphere with that same radius! Ready? ")
vol_sphere = (4 / 3) * pi * r ** 3
print("\nThe volume of a sphere with radius", r, "is", vol_sphere, "cubic inches!")

print("\nThat is enough for today.\n\nGoodbye.\n")
