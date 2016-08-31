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

def main():
    print("Let's discover how many years it will take for a given principle to reach a savings goal, using compound interest.")
    principle = int(input("What is the initial principle? "))
    rate = float(input("What is the interest rate, expressed in a decimal? "))
    goal = int(input("And what is the savings goal? "))
    years = 0
    while principle < goal:
        principle += (principle * rate)
        years += 1
    print("Given those parameters, it would take", years, "years...")

main()
