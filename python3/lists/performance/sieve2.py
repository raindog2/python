#!/usr/bin/env python3.2

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


def sieve2(n):
    primes = [True] * n 
    for k in range(2, n+1):
        if primes[k-1] == True:
            for j in range(2*k, n+1, k):
                if primes[j-1] == True:
                    primes[j-1] = False
    return primes

def main():
    n = int(input("Enter the top number for our list of primes: "))
    global start_time 
    start_time = time.time()
    print("The list of primes up to", n, "are:\n", sieve2(n))

main()

print(time.time() - start_time, "elapsed.")
