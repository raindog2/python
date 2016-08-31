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

def F2C(x):
    return (x - 32) * 0.5555555

def C2F(x):
    return x * 1.8 + 32

def C2K(x):
    return x + 273

def main():
    fahr = float(input("Let's convert that F to C! What is the F? "))
    print("That F would be", F2C(fahr), "in C")
    celsius = float(input("Let's convert a C to F, for the non-Canadians. What is the C? "))
    print("That C would be", C2F(celsius), "in F")
    print("...and, even though you didn't ask, that would be", C2K(celsius), "in Kelvin")

main()

