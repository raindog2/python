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
from random import choice
from random import randint

def swap(items, i, j):
    hold = items[i]
    items[i] = items[j]
    items[j] = hold
    return items

def myreverse(items):
    items = items[::-1]
    return items

def my_shuffle(items):
    n = len(items)
    for i in range(n-2):
        items = swap(items, i, randint(i, n-1))
    return items
           
def is_sorted(items):
    for i in range(len(items)-1):
        if items[i] > items[i+1]: return False
        else: continue
    return True

#SORTING USING SWAP
def sort_list(items):
    for i in range(len(items)-1):
        if items[i] == min(items[i:]): continue
        else: items = swap(items, i, items.index(min(items[i:])))
        #print(items)
        #print(is_sorted(items))
    return items

#SORTING USING SWAP
#def sort_list(items):
    #for i in items:
        #if i == min(items[items.index(i):]): continue
        #else: items = swap(items, items.index(i), items.index(min(items[items.index(i):])))
    #return items

#CHEATING--SORTING NOT USING SWAP
#def sort_list(items):
    #result = []
    #for i in range(len(items)):
       #result.append(min(items)) 
       #items.remove(min(items))
    #return result

def main():
    print("SWAPS")
    print(swap([1,2,3,4,5], 2, -1))
    print(swap(['a','b','c','d','e'], 1, 4))
    print(swap([2,4,6,8,10,12,14,16], 1, 7))
    print("REVERSES")
    print(myreverse([1,2,3,4,5]))
    print(myreverse([x**2 for x in range(10)]))
    print("SHUFFLES")
    print(my_shuffle([1,2,3,4,5]))
    print(my_shuffle([x**2 for x in range(10)]))
    print(my_shuffle([x for x in range(100)]))
    print(my_shuffle([x+3 for x in range(100) if x % 3 == 0]))
    print("IS SORTED")
    print(is_sorted([x**2 for x in range(10)]))
    print(is_sorted(my_shuffle([x**2 for x in range(10)])))
    print(is_sorted([1,2,3,4,5,4]))
    print(is_sorted([4]))
    print(is_sorted([]))
    print("SORT")
    x = [x for x in range(30)] 
    print(my_shuffle(x))
    print(sort_list(my_shuffle(x)))
    #print(sort_list([randint(1,99) for num in range(100)]))
    
main()

