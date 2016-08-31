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

from math import pow
from math import sqrt
import os
os.system('clear')

def square_root1(k):
    x = 1
    while abs(x ** 2 - k) >= 1E-10:
        x = (x + k / x) / 2
    return x

def square_root5(k):
    x = 5
    while abs(x ** 2 - k) >= 1E-10:
        x = (x + k / x) / 2
    return x

def square_root10(k):
    x = 10
    while abs(x ** 2 - k) >= 1E-10:
        x = (x + k / x) / 2
    return x

def square_root15(k):
    x = 15
    while abs(x ** 2 - k) >= 1E-10:
        x = (x + k / x) / 2
    return x

#def main():
#    k = int(input("What number would you like to find the square root of?\n> "))
#    print(square_root(k))

def main():
    for i in range (2, 26):
        print("The square root of", i, "with intial guess 1 is about ", round(square_root1(i), 5))
        print("The square root of", i, "with intial guess 5 is about ", round(square_root5(i), 5))
        print("The square root of", i, "with intial guess 10 is about", round(square_root10(i), 5))
        print("The square root of", i, "with intial guess 15 is about", round(square_root15(i), 5))
        print("The square root of", i, "is exactly                   ", round(sqrt(i), 5),"\n")
        
main()
