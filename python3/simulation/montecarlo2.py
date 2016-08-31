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

#import os
#os.system('clear')
from random import uniform
from math import exp

def estimate_area(f, a, b, m, n=10000):
    #Estimate area under f(x) for an x value between a and b 
    #and a y value between 0 and m, with n as the number of tries

    #Number of estimations below the curve (in the area)
    hits = 0
    #Total area of the rectangle surrounding the curve
    total = m * (b - a)
    #Generate a try, i.e. a random point on the graph
    for i in range(n):
        #Let x be a random number on the x axis
        x = uniform(a, b)
        #Let x be a random number on the y axis
        y = uniform(0, m)
        #If the y coordinate of the estimation is less than the value of 
        #the function (i.e. below the curve) then add a hit to the total hits
        if y <= f(x):
            hits += 1
    #The percent hits of total tries
    frac = hits / n
    #Find the area under the curve by multiplying the total area of the rectangle
    #by the percent of tries that were hits (i.e. x% of tries were hits because x%
    #of the area of the rectangle is under the curve)
    return n, frac * total

#The function that generates the value of each point on the curve--becomes
#"f" in estimate_area
def f(x):
    return x ** 3 + x ** 2 

def main():
    #Run estimate_area using n = 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000 
#    for i in range(1, 10):
#        print(estimate_area(f, 0, 2, 1, 10 ** i))

    #Run estimate_value 25 times using the default n=10000
    for i in range(1, 26):
        print(estimate_area(f, -1, 1, 1))

main()
