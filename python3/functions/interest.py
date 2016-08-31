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

# This program is written for Python3.2
# It uses Heron's Formula to find the area of the triangle given the
# length of the three sides...https://en.wikipedia.org/wiki/Heron's_formula

from math import sqrt
import os
os.system('clear')

def new_balance(P, r, t):
    return P * (1 + r) ** t


def main():
    print("Let's figure out the new balance on a compound-interest savings account, given the starting principle, interest rate, and number of years...")
    P = float(input("What is the starting principle, in dollars? "))
    r = float(input("What is the interest rate, expressed as a decimal? "))
    t = int(input("How many years do you want to compute? "))
    print("So given that information, the new balance would be", new_balance(P, r, t), "dollars")

main()
