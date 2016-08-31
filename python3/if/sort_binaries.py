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

def sort(x, y, z):
    if x >= y >= z:
        print(z, y, x)
    if x >= z >= y:
        print(y, z, x)
    if y >= z >= x:
        print(x, z, y)
    if y >= x >= z:
        print(z, x, y)
    if z >= y >= x:
        print(x, y, z)
    if z >= x >= y:
        print(y, x, z)

def main():
    print("Give me an x, y, and z, each an integer...\n")
    x = int(input("What is x? "))
    x = bin(x)
    y = int(input("What is y? "))
    y = bin(y)
    z = int(input("What is z? "))
    z = bin(z)
    print("Converting to binary numbers and sorting, lowest to highest........")
    return sort(x, y, z)

main()
