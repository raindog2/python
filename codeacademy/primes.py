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

def is_prime(x):
    if x <= 1:
        return False
    #elif x == 2:
        #return True
    total = 0
    half = x / 2
    if x < 10:
        for n in range(1, x + 1):
            if x % n == 0:
                total += 1
            else:
                total += 0
        if total <= 2:
            return True
        else:
            return False
    else:
        for n in range(1, half + 1):
            if x % n == 0:
                total += 1
            else:
                total += 0
        if total <= 1:
            return True
        else:
            return False
        
num = int(raw_input("Count the primes between 1 and ? "))
total_prime = 0
for x in range(num):
    print x, is_prime(x)
    if is_prime(x) == True:
        total_prime += 1
    else:
        total_prime += 0
        
print "Total prime numbers between 1 and %s is: %s" % (num, total_prime)
