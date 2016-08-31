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
import time
os.system('clear')

start_time = time.time()

def find_proper_divisors(n):
    divisors = [1]
    for i in range(2, n//2+1):
        if n % i == 0:  divisors.append(i)
    return divisors

def is_perfect(n):
    sum = 0
    for i in find_proper_divisors(n):
        sum += i
    if sum == n: return True
    else: return False

def main():
    #for i in range(2, 101):
        #print("For", i, "the proper divisors are:", find_proper_divisors(i))
    print("The perfect numbers less than 10000 are:")
    for i in range(2, 10001):
        if is_perfect(i): print(i)
    #for i in range(2, 100):
        #print(i,":",isprime(i))
    #for i in range(2,100):
        #print(i, ":", primefactorization(i))
main()

print(time.time() - start_time, "elapsed.")
