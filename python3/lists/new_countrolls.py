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
#import time
from random import choice

def roll():
    dice = [1,2,3,4,5,6]
    return choice(dice)

def main():
    totals = [0,0,0,0,0,0]
    rolls = int(input("How many times do you want to roll?\n> "))
    for i in range(0, rolls):
        if roll() == 1:
            print("Roll......ONE!")
            totals[0] += 1
        elif roll() == 2:
            print("Roll......TWO!")
            totals[1] += 1
        elif roll() == 3:
            print("Roll......THREE!")
            totals[2] += 1
        elif roll() == 4:
            print("Roll......FOUR!")
            totals[3] += 1
        elif roll() == 5:
            print("Roll......FIVE!")
            totals[4] += 1
        else:
            print("Roll......SIX!")
            totals[5] += 1
#The else category, for some reason, ends up with a lot more rolls recorded than it should...like 40% consistently
    print("All told, we saw:\n", totals[0], "ones, or", totals[0] / rolls * 100, "%\n", 
            totals[1], "twos, or", totals[1] / rolls * 100, "%\n", 
            totals[2], "threes, or", totals[2] / rolls * 100, "%\n", 
            totals[3], "fours, or", totals[3] / rolls * 100, "%\n", 
            totals[4], "fives, or", totals[4] / rolls * 100, "%\n", 
            totals[5], "sixes, or", totals[5] / rolls * 100, "%!!")

main()
