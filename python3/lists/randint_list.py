#!/usr/bin/env python3.4

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
from random import choice

def randints(n,a,b):
    deliverable = []
    pool = list(range(a, b+1))
    for i in range(n):
        deliverable.append(choice(pool))
    return deliverable

def randfloats(n,a,b):
    deliverable = []
    pool = []
    for i in range(a, b+1):
        pool.append(float (i))
    for i in range(n):
        deliverable.append(choice(pool))
    return deliverable

def randintsDistinct(n,a,b):
    if n > (b + 1 - a):
        print("List size cannot be greater than amount of numbers in range, and so I will return the dreaded:")
    else:
        deliverable = []
        pool = list(range(a, b+1))
        i = 0
        while i < n:
            num = choice(pool)
            if num not in deliverable:
                deliverable.append(num)
                i += 1
        return deliverable

def main():
    print("FLOATS")
    print(randfloats(5, 10, 100),"\n")
    print(randfloats(8, 1, 7),"\n")
    print(randfloats(0, -12, 0),"\n")
    print(randfloats(4, -12, 0),"\n")
    print("INTS")
    print(randintsDistinct(5, 10, 100),"\n")
    print(randintsDistinct(8, 1, 7),"\n")
    print(randintsDistinct(0, -12, 0),"\n")
    print(randintsDistinct(4, -12, 0),"\n")

#def main():
    #print(randints(5, 10, 100),"\n")
    #print(randints(100, 1, 7),"\n")
    #print(randints(0, -12, 0),"\n")
    #print(randints(4, -12, 0),"\n")

main()

