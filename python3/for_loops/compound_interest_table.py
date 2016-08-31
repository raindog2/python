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

#clunkier approach that breaks up the math into seperate functions...

def new_balance(P, r, t, n):
    return P * (1 + r / n)**(n*t)

def main():
    print("Let's discover the effect of compound interest.  You give me the initial balance, an interest rate, and a number of years.  I will compute the new balance for a range of different compound interest scenarios.")
    P = float(input("What is your current balance? "))
    r = float(input("What is the interest rate (expressed as a decimal)? "))
    t = float(input("What is the number of years? "))
    for x in range(1, 13):
        print("For interest compounded", x, "times per year, the new balance would be", new_balance(P, r, t, x))

main()

