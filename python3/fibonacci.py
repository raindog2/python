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

import time
import os
os.system('clear')
from math import sqrt

#def fibonacci(n):
#    if n == 0:
#        return 1
#    else:
#        return fibonacci(n - 1) + fibonacci(n - 2)
def fibonacci(n):
    return int(((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5)))

print("This program will print a Fibonacci sequence, starting from the point in the sequence you choose.")
print("What I need from you is the ordinal position in the sequence you would like to start from (e.g. 10th number, 24th number, etc.)")
x = int(input("Please give me that ordinal position as an integer (i.e. say '10' for the 10th position, etc.)\n> "))
print("OK, we will start from position", x, "in the Fibonacci sequence...")
for i in range (x, x + 100):
    print(fibonacci(i),"...")
    time.sleep(1)
