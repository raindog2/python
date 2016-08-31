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

def max3(x, y, z):
    if y > x > z or z > x > y:
        print("The middle value is", x)
    if y > z > x or x > z > y:
        print("The middle value is", z)
    if z > y > x or x > y > z:
        print("The middle value is", y)
    if z == x or y == x:
        print("The middle value is", x)
    if z == y :
        print("The middle value is", y)

def main():
    print("Give me an x, y, and z, each an integer...\n")
    x = int(input("What is x? "))
    y = int(input("What is y? "))
    z = int(input("What is z? "))
    return max3(x, y, z)

main()

