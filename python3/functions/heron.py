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
# It uses Heron's Formula to find the area of the triangle given the
# length of the three sides...https://en.wikipedia.org/wiki/Heron's_formula

from math import sqrt
import os
os.system('clear')

def area(x, y, z):
    s = (x + y + z) / 2
    return sqrt ( s * (s - x) * (s - y) * ( s - z))

def main():
    print("Finding the area of the triangle given the length of each side...")
    a = float(input("What is the length of the first side, in inches? "))
    b = float(input("What is the length of the second side, in inches? "))
    c = float(input("What is the length of the third side, in inches? "))
    print("Awesome: the area would be", area(a, b, c), "sq. inches")
    
main()
