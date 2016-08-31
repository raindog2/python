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

def myfactorial(n):
    product = 1
    for k in range(1, n + 1):
        product *= k
    return product

def mypower(n):
    return n ** 2

def myexponential(n):
    return 2 ** n

def main():
    users_number = int(input("What number would you like to find the factorial of? "))
    for k in range(1, users_number +1):
        print(k)
        print("Factorial:", myfactorial(k))
        print("Squared:", mypower(k))
        print("2 raised to the power of", k,":", myexponential(k), "\n")

main()
