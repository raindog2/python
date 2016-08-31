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

from math import sqrt
import os
os.system('clear')

def hypot(x, y):
    return sqrt(x ** 2 + y ** 2)

def main():
    print("Let's figure out the hypoteneuse of a triangle given the length of the sides!") 
    a = float(input("Length of side a (in inches): "))
    b = float(input("Length of side b (in inches): "))
    answer = hypot(a, b)
    print("The length of the hypoteneuse is", answer, "inches!")
    
main()
