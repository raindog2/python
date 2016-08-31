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

def isprime(n):
    #Return True if n is prime
    return n > 1 and smallestdivisor(n)

def smallestdivisor(n):
    #Find smallest divisor (other than 1) of integer n > 1
    for k in range(2, int(sqrt(n))+1):
        if divides(k, n):
            return False
        else:
            return True
    #This is the original while loop
    #while k < sqrt(n) and not divides(k, n):
    #    k += 1
    #return k 

def divides(k, n):
    #Return True if k divides n
    return n % k == 0

def main():
    for n in range(2, 400):
        if isprime(n):
            print(n, end=" ")
    print()

main()

