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

def zone(age, rate):
    m = max_heart(age)
    if rate >= m * 0.9:
        print("Interval Training")
    if m * 0.9 > rate >= m * 0.7:
        print("threshold training")
    if m * 0.7 > rate >= m * 0.5:
        print("aerobic training")
    if m * 0.5 > rate:
        print("Couch potato")

def max_heart(age):
    return 208 - 0.7 * age

def main():
    print("Let's discover your current training zone based on your age and your current training heart rate...")
    age = float(input("What is your age? "))
    rate = float(input("What is your current heart rate? "))
    return zone(age, rate)

main()
