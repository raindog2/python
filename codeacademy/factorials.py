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

# NB: Written in PYTHON 2!!!

def factorial(x):
    total = 0
    if x == 1:
        return x
    else:
        s = 1
        for i in range(2, x + 1):
            s *= i
    return s

def factorial1(x):
    total = 1
    while x > 1:
       total *= x
       x = x - 1
    return total
 
num = int(raw_input("What is the #? "))
print factorial(num)
print factorial1(num)
