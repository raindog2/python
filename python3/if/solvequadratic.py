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

print("Welcome to the python quadratic formula solver!\n")

def solvequadratic(a, b, c):
    
    d = b ** 2 - 4 * a * c
    
    if d < 0:
        print("With those values there are no solutions")

    if d == 0:
        x = -b / 2 * a
        print("There is one solution:", x)
    
    if d > 0:
        x1 = (-b + sqrt(b ** 2 - 4 * a * c))/2 * a
        x2 = (-b - sqrt(b ** 2 - 4 * a * c))/2 * a
        print("There are two solutions:", x1, x2)

def main():
    
    a = int(input("Give me a value for a "))
    b = int(input("Give me a value for b "))
    c = int(input("Give me a value for c "))
    
    return solvequadratic(a, b, c)

main()
