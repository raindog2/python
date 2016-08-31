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

def isprime(n):
    if n <= 3: return True
    else: 
        for i in range(2, n//2+1):
            if n % i == 0: return False
    return True

def generate_plist(n):
    plist = []
    for i in range(2,n):
        if isprime(i): plist.append(i)
    return plist

def generate_blist(n):
    blist = [True] * n 
    for k in range(2, n+1):
        if blist[k-1] == True:
            for j in range(2*k, n+1, k):
                if blist[j-1] == True:
                    blist[j-1] = False
    blist.remove(blist[0])
    return blist

def test(plist, blist, n):
    count = 0
    for i in blist:
        if i == True: count += 1
    if count == len(plist): return True
    else: return False

def main():
    n = int(input("Enter the top number for our list of primes: "))
    print("PLIST: ", generate_plist(n))
    print("BLIST: ", generate_blist(n))
    print(test(generate_plist(n), generate_blist(n), n))

main()
