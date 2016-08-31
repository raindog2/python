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

def rate_over_times_per_year(r, n):
    return r / n

def years_times_number_of_times_per_year(n, t):
    return n * t

def new_balance(P):
    return P * (1 + rate_over_times_per_year(r, n)) ** years_times_number_of_times_per_year(n, t)

def main():
    print("Let's determine your new savings balance after compound interest, given an initial balance, an interest rate, a number of years, and the number of times per year the interest is compounded.")
    P = float(input("What is your current balance? "))
    r = float(input("What is the interest rate (expressed as a decimal)? "))
    t = float(input("What is the number of years? "))
    n = float(input("How many times per year is the interest compounded? "))
    print("Given those values, the new balance is $",new_balance(P))

main()
    
