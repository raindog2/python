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
    cents = int(input("What is the total number of cents? "))
    dollars = cents // 100
    quarters = (cents % 100) // 25
    dimes = (cents % 100) % 25 // 10
    nickels = (((cents % 100) % 25) % 10) // 5
    pennies = (((cents % 100) % 25) % 10) % 5
    print("That would be:\n", dollars, "dollars\n", quarters, "quarters\n", dimes, "dimes\n", nickels, "nickels and\n", pennies, "pennies!!!")

main()

