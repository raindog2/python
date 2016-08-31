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
os.system('clear')
from random import randint

def mean(items):
    return float(sum(items))/len(items)

def median(items):
    itemsmedian = items[:]
    itemsmedian.sort() 
    print(itemsmedian)
    index = int(len(itemsmedian)/2)
    if len(itemsmedian) % 2 != 0:
        return itemsmedian[index]
    else:
        return (itemsmedian[index] + itemsmedian[index-1])/2

def mymin(items):
    answer = []
    itemsmin = items[:]
    while len(itemsmin) > 1:
        if itemsmin[0] <= itemsmin[1]:
            answer = [itemsmin[0]]
            itemsmin.remove(itemsmin[1])
        else:
            answer = [itemsmin[1]]
            itemsmin.remove(itemsmin[0])
    return answer[0] 

def mymax(items):
    answer = []
    itemsmax = items[:]
    while len(itemsmax) > 1:
        if itemsmax[0] >= itemsmax[1]:
            answer = [itemsmax[0]]
            itemsmax.remove(itemsmax[1])
        else:
            answer = [itemsmax[1]]
            itemsmax.remove(itemsmax[0])
    return answer[0] 

random_list = []
for i in range (8):
    random_list.append(randint(0,35))

def main():
    print(random_list)
    print("Mymax sez:", mymax(random_list))
    print("Max sez:", max(random_list))
    print("Mymin sez:", mymin(random_list))
    print("Min sez:", min(random_list))
    print("Mean sez:", mean(random_list))
    print("Median sez:", median(random_list))

main()
