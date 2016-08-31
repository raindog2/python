#!/usr/bIn/env python

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

def grade(score):
    if score >= 90:
        print("That score is an A!")
    if 90 > score >= 80:
        print("That score is a B!")
    if 80 > score >= 70:
        print("That score is a C!")
    if 70 > score >= 60:
        print("That score is a D!")
    if 60 > score:
        print("That score is an F!")

def main():
    score = float(input("What is the score? "))
    return grade(score)

main()
