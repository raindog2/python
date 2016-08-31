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

# NB: Written in PYTHON 2!!!

print "Select the Mutt colorscheme that is right for you!"
ans = int(raw_input("Would you prefer light (1) or dark (2)? "))
if ans == 1:
    f = open("/home/mpurcell/muttrc_cadaver", "r+")
    for line in f:
        f.readline()
        if line == "source ~/.mutt/color_black":
            line = "#source ~/.mutt/color_black"
        elif line == "#source ~/.mutt/color_light":
            line = "source ~/.mutt/color_light"
    f.close()
else:
    f = open("/home/mpurcell/muttrc_cadaver", "r+")
    for line in f:
        if line == "source ~/.mutt/color_white":
            line = "#source ~/.mutt/color_white"
        elif line == "#source  ~/.mutt/color_black":
            line = "source ~/.mutt/color_black"
    f.close()


