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

def pyramid(n):
    sum = 0
    for k in range(1, n + 1):
        sum += k ** 2
    return sum

def main():
    for k in range(1, 21):
        print("For", k, "the result would be", pyramid(k))
        print("And the added value is", pyramid(k) - pyramid(k-1),"\n")

main()
