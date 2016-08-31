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

def create_username(firstname, lastname):
    username = firstname.lower()[0] + lastname.lower()[:7]
    return username
    #username = lastname.lower()[:12] + firstname.lower()[0] + "1"
    #return username

def main():
    print("Let's create a username from your name!")
    firstname = input("What is your first name? ")
    lastname = input("What is your last name? ")
    print("Your new username is", create_username(firstname, lastname), "!!")

main()


