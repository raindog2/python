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

from math import log
import os
os.system('clear')

def main():
    for x in range(10, 201, 10):
        logarithm = log(x)
        nlogn = x * log(x)
        nn = x ** 2
        two_n = 2 ** x
        print(x, logarithm, nlogn, nn, two_n)

main()
