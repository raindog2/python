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

def smallestdivisor(n):
    k = 2
    while k <  n and not divides(k,n):
        k += 1
    return k

def divides(k, n):
    return n % k == 0

#def primefactorization(n):
    #result = [1]
    #if isprime(n):
        #result.append(n)
        #return result
    #else: 
        #for i in range(2,n/2+1):
            #if isprime(i): result.append(i)
            #else continue
        #return result
        #first = int(n / smallestdivisor(n))
        #second = int(smallestdivisor(first))
        #third = int(smallestdivisor(second))
        #fourth = int(smallestdivisor(third))
        #fifth = int(smallestdivisor(fourth))
        #result.append(smallestdivisor(n))
        #if isprime(first): result.append(first)
        #else: 
            #result.append(second)
            #if isprime(second): result.append(second)
            #else:
                #result.append(third)
                #if isprime(third): result.append(third)
                #else: 
                    #result.append(fourth)
                    #if isprime(fourth): result.append(fourth)
                    #else: result.append(fifth)
                #....

    #return result  
        #if isprime(smallestdivisor(n)): 
            #result.append(smallestdivisor(n))
            #if isprime(smallestdivisor(n/smallestdivisor(n))):
                #result.append(smallestdivisor(n/smallestdivisor(n)))
      
        
        #for i in range(n):
            #if n % i == 0 and isprime(i): result.append[i]
            #elif n % i == 0 and not isprime(i): 

def primefactors(n):
    factors = [1]
    for i in range(2, n+1):
        if n % i == 0 and isprime(i): factors.append(i)
    return factors

def main():
    for i in range(2, 101):
        print("For", i, "the prime factors are:", primefactors(i))
    #for i in range(2, 100):
        #print(i,":",isprime(i))
    #for i in range(2,100):
        #print(i, ":", primefactorization(i))
main()

