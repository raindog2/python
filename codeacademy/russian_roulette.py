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

# NB: Written in PYTHON 2!!!

import os
os.system('clear')
import random

print "Russian Roulette!"
print "One bullet will be in a gun with six chambers."
print "The trigger will be pulled 3 times."
print "If the chamber contains the bullet, you lose!"

count = 1
while count < 4:
    ready = raw_input("Ready? ")
    print "Shot " + str(count) + "..."
    num = random.randint(1, 6)
    if num != 5:
        print "Click."
    elif num == 5:
        print "BANG! You lose!"
        break
    count += 1
else:
    print "You win!"
