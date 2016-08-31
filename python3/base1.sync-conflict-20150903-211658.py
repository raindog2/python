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

def harmonic(n):
    # compute the sum of 1/k**2 for k=1 to n.
    total = 0 
    for k in range(1, n + 1):
        total += 1 / k ** 2
        print("For", k, "the total is", total)

def main():
    n = int(input("Enter a postive integer: "))
    harmonic(n)

main()
