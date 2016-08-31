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

def divides(k, n):
    return n % k == 0

#def list_of_factors(n):
    #factors = []
    #for i in range(2,n):
        #if divides(i,n): factors.append(i)
    #return factors

#def test_if_done(lst, n):
    #product = 1
    #for i in lst:
        #product *= i
    #if product == n: return True 
    #else: return False

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

def primefactorization(n):
    prime_factors = []
    if isprime(n): 
        return "PRIME!!"
        #print("PRIME!!")
    else:
        while n > 1:
            prime_factors.append(smallestdivisor(n))
            n = n / smallestdivisor(n)
        return prime_factors

    #factors = list_of_factors(n) 
    #for i in factors:
        #if isprime(i): 
            #prime_factors.append(i)
            #if test_if_done(prime_factors, n): return prime_factors
        #else:
            #new_list = list_of_factors(i)
            #for i in new_list:
                #if isprime(i):
                    #prime_factors.append(i)
                    #if test_if_done(prime_factors, n): return prime_factors
                #else:
                    #new_list2 = list_of_factors(i)
                    #for i in new_list2:
                        #if isprime(i):
                            #prime_factors.append(i)
                            #if test_if_done(prime_factors, n): return prime_factors
                        #else:
                            #new_list3 = list_of_factors(i)
                            #for i in new_list3:
                                #if isprime(i):
                                    #prime_factors.append(i)
                                    #if test_if_done(prime_factors, n): return prime_factors
                                    #else:



                #if isprime(i): prime_factors.append(i)
                #else: 
                    #new_list2 = list_of_factors(i)
                    #for i in new_list2:
                        #if isprime(i): prime_factors.append(i)
                        #else: print("Whew!!")
    #return prime_factors


#def primefactors(n):
    #factors = [1]
    #for i in range(2, n+1):
        #if n % i == 0 and isprime(i): factors.append(i)
    #return factors

def main():
    #for i in range(2, 101):
        #print("For", i, "the prime factors are:", primefactors(i))
    #for i in range(2, 100):
        #print(i,":",isprime(i))
    for i in range(2,100001):
        print(i, ":", primefactorization(i), end=" -- ")
main()

print(time.time() - start_time, "elapsed.")
