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
from random import randint

def roll():
    return randint(1, 6)
#def roll():
#    x = randint(1, 6)
#    return x

def main():
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    rolls = int(input("How many times do you want to roll?\n> "))
    for i in range(0, rolls):
        #time.sleep(1)
        if roll() == 1:
            print("Roll......ONE!")
            ones += 1
        elif roll() == 2:
            print("Roll......TWO!")
            twos += 1
        elif roll() == 6:
            print("Roll......SIX!")
            sixes += 1
        elif roll() == 4:
            print("Roll......FOUR!")
            fours += 1
        elif roll() == 5:
            print("Roll......FIVE!")
            fives += 1
#The else category, for some reason, ends up with a lot more rolls recorded than it should...like 40% consistently
        else:
            print("Roll......THREE!")
            threes += 1
    print("All told, we saw:\n", ones, "ones, or", ones / rolls * 100, "%\n", 
            twos, "twos, or", twos / rolls * 100, "%\n", 
            threes, "threes, or", threes / rolls * 100, "%\n", 
            fours, "fours, or", fours / rolls * 100, "%\n", 
            fives, "fives, or", fives / rolls * 100, "%\n", 
            sixes, "sixes, or", sixes / rolls * 100, "%!!")

main()
