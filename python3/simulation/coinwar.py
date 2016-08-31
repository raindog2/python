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
import time
from random import randint

def main():
#Welcome message
    print("\n==========WELCOME TO COIN WAR!!!==========\n")
    print("In this game, each player has a certain number of coins.\nFor each round, each player flips a coin.\nIf the results are the same (heads-heads or tails-tails), Player 1 wins boths coins.\nIf the results are different (heads-tails or tails-heads), Player 2 wins both coins.\nThe rounds continue until one player has lost all his or her coins.\n")

#Define some variables
    player1 = input("What is the name of Player 1?\n> ")
    player2 = input("What is the name of Player 2?\n> ")
    coins = int(input("How many coins do you want each player to start with?\n> "))
    player1_coins = coins
    player2_coins = coins
    round_number = 1

#The main engine (a while loop)
    while player1_coins != 0 and player2_coins != 0:
        x = randint(0, 1)
        y = randint(0, 1)
        print("\nHere we go with Round", round_number, "!!!")
        if x == y:
            print("The coins were the same, and so", player1, "wins the round!")
            player1_coins += 1
            player2_coins -= 1
        if x != y:
            print("The coins were different, and so", player2, "wins the round!")
            player1_coins -= 1
            player2_coins += 1
        print(player1, "has", player1_coins, "coins")
        print(player2, "has", player2_coins, "coins")
        round_number += 1
        #input("Press <ENTER> to continue")
        #time.sleep(4)

#The end game
    if player1_coins == 0:
        print("\nCongratulations to our winner,", player2, "!!!\n")
    if player2_coins == 0:
        print("\nCongratulations to our winner,", player1, "!!!\n")

main()    
