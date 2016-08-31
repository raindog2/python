#!/usr/bin/env python3.2

# Copyright (C) 2015 Mark Purcell <mpurcell@uw.edu>

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

def init(left, right, inittemp, n):
    bar_temps = [inittemp] * (n + 1)
    bar_temps[0] = left
    bar_temps[-1] = right
    return bar_temps

def main():
    init_temps = init(50,50,0,10)
    #init_temps = init(30,50,0,10)
    rod_length = 5
    segments = 10
    duration = 10
    dt = ((rod_length / segments) ** 2) / 2
    iteration = 1
    
    print("Initial temps at the ends of the segments:", init_temps)
    print("Bar length:", rod_length, "cm")
    print("Segments:", segments)
    print("Duration of simulation:", duration, "seconds\n")

    while iteration < (duration / dt + 1):
        for i in range(1,10):
            init_temps[i] = (init_temps[i-1] + init_temps[i+1]) / 2
        init_temps = init_temps[:]
        print("After", dt * iteration, "seconds the temps are:", init_temps)
        #print("Iteration:", iteration, init_temps)
        iteration += 1

main()

print()
print (time.time() - start_time, "elapsed.\n")
