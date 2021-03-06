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

def main():
    import os
    os.system('clear')
    found = False
    min = 1
    max = int(input("I will guess an integer between 1 and an upper limit of your choosing.  What would you like the upper limit to be? \n>"))
    guess = (max - min) // 2
    guess_number = 1
    while not found:
        print("Is the number", guess,"?")
        feedback = int(input("Enter 1 if the number is higher\nEnter 2 if the number is lower\nEnter 3 if that is correct\n>"))
        if feedback == 1:
            min = guess
            guess += (max - min) // 2
            guess_number +=1
        elif feedback == 2:
            max = guess
            guess -= (max - min) // 2
            guess_number +=1
        else:
            print("I did it!!\nI used", guess_number, "guesses.")
            again = input("Would you like to play again (y/n)?")
            if again == "y" or again == "yes":
                main()
            else:
                print("OK, thanks for playing!")
                found = True
                exit()
main()
