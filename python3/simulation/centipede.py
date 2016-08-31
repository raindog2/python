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
from random import randint

from turtle import *

def centipede(length, step, life):
    penup()
    theta = 0
    dtheta = 1
    for i in range(life):
        forward(step)
        left(theta)
        theta += dtheta
        stamp()
        if i > length:
            clearstamps(1)
        if abs(theta) > randint(4, 16):
            dtheta = -dtheta
        if abs(ycor()) > 380:
            left(30)
        if abs(xcor()) > 350:
            left(30)

def main():
    setworldcoordinates(-400, -400, 400, 400)
    centipede (14, 10, 400)
    exitonclick()

main()

