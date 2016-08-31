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

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "\nLet's play Battleship!"
print "Here is a map of the board:"
print_board(board)
print "Each battleship is one 'O' big"

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_row2 = random_row(board)
ship_row3 = random_row(board)

ship_col = random_col(board)
ship_col2 = random_col(board)
ship_col3 = random_col(board)

if (ship_row == ship_row2 and ship_col == ship_col2) and ship_row != 4:
    ship_row += 1
elif (ship_row == ship_row2 and ship_col == ship_col2) and ship_row == 4:
    ship_row -= 1
elif (ship_row == ship_row3 and ship_col == ship_col3) and ship_row != 4:
    ship_row += 1
elif (ship_row == ship_row3 and ship_col == ship_col3) and ship_row == 4:
    ship_row -= 1
elif (ship_row2 == ship_row3 and ship_col2 == ship_col3) and ship_row2 != 4:
    ship_row2 +=1
elif (ship_row2 == ship_row3 and ship_col2 == ship_col3) and ship_row2 == 4:
    ship_row2 -=1

#The next two lines tell the user the answer, useful only for debugging:
#print ship_row + 1
#print ship_col + 1
#print ship_row2 + 1
#print ship_col2 + 1
#print ship_row3 + 1
#print ship_col3 + 1

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!

battleships_sunk = 0

for turn in range(6):
    if battleships_sunk < 3:
        print "\nGuess", turn + 1
        guess_row = int(raw_input("Guess Row (1-5):"))
        guess_col = int(raw_input("Guess Col (1-5):"))
        
        guess_row -=1
        guess_col -=1

        if guess_row == ship_row and guess_col == ship_col:
            print "Congratulations! You sunk battleship one!\n"
            battleships_sunk += 1
            board[guess_row][guess_col] = "B"
            ship_row = "dead"
            ship_col = "dead"
        elif guess_row == ship_row2 and guess_col == ship_col2:
            print "Congratulations! You sunk battleship two!\n"
            battleships_sunk += 1
            board[guess_row][guess_col] = "B"
            ship_row2 = "dead"
            ship_col2 = "dead"
        elif guess_row == ship_row3 and guess_col == ship_col3:
            print "Congratulations! You sunk battleship three!\n"
            battleships_sunk += 1
            board[guess_row][guess_col] = "B"
            ship_row3 = "dead"
            ship_col3 = "dead"
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print "\nOops, that's not even in the ocean.\n"
                if turn == 5:
                    print "Game Over\n"
            elif(board[guess_row][guess_col] == "X" or board[guess_row][guess_col] == "B"):
                print "\nYou guessed that one already.\n"
                if turn == 5:
                    print "Game Over\n"
            else:
                print "\nYou missed all battleships!\n"
                board[guess_row][guess_col] = "X"
                if turn == 5:
                    print "Game Over\n"
    else:
        print "\nYou sank all 3!!!\n"
        break

    # Print (turn + 1) here!
    print "A summary of your guesses: "
    print_board(board)
