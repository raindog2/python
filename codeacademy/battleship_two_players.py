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

from random import randint
import os
os.system('clear')

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "\nLet's play Battleship!"
print "Here is a map of the board:"
print_board(board)

player1_name = raw_input("Player 1 Name: ")
player2_name = raw_input("Player 2 Name: ")

print "\nOK, " + player1_name + ", you will enter the row and column of the battleship while " + player2_name + " looks away..."

ship_row = int(raw_input("Enter row of battleship (1-5):"))
ship_row -= 1
ship_col = int(raw_input("Enter column of battleship (1-5):"))
ship_col -= 1

os.system('clear')

#def random_row(board):
    #return randint(0, len(board) - 1)

#def random_col(board):
    #return randint(0, len(board[0]) - 1)

#ship_row = random_row(board)
#ship_col = random_col(board)
#The next two lines tell the user the answer, useful only for debugging:
#print ship_row
#print ship_col

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!


print "\nOK, " + player2_name + ", time to guess.  You have 4 guesses."
print "Here is a map of the board:"
print_board(board)

for turn in range(4):
    print "\nTurn", turn + 1
    guess_row = int(raw_input("Guess Row (1-5):"))
    guess_col = int(raw_input("Guess Col (1-5):"))
    
    guess_row -=1
    guess_col -=1

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk the battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "\nOops, that's not even in the ocean.\n"
            if turn == 3:
                print "Game Over\n"
        elif(board[guess_row][guess_col] == "X"):
            print "\nYou guessed that one already.\n"
            if turn == 3:
                print "Game Over\n"
        else:
            print "\nYou missed the battleship!\n"
            board[guess_row][guess_col] = "X"
            if turn == 3:
                print "Game Over\n"
                print "The battleship was at row " + str(ship_row + 1) + " column " + str(ship_col + 1)
        
    # Print (turn + 1) here!
    print "A summary of your guesses: "
    print_board(board)
