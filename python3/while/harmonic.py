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

def harmonic(m):
    total = 0
    #this is not working: it never judges total to be >= m
    while m > total:
        for i in range(1, 10500):
            total += 1 / i
    return k - 1

def main():
    m = int(input("Enter a postive integer: "))
    print("The smallest integer k such that the sum of sigma 1/k is >=", m, "is", harmonic(m))

main()
