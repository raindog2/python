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

def exponent_part(t):
    return 17.67 * t / (t + 243.5)

def main_calc(t):
    return 6.112 ** exponent_part(t)
    
def main():
    print("Hi...let's discover the estimated vapor pressure of water vapor in millibars for a range of temperatures in C!!")
    for x in range(-20, 50, 5):
        print("Given temperature", x, "C, the estimated vapor pressure of water vapor in millibars is:", main_calc(x))
    
main()
