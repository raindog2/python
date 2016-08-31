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
print "The Battleship is three spaces long."

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

row_or_col = randint(0, 1)

ship_row = random_row(board)
ship_col = random_col(board)

if row_or_col == 0:
    if ship_row <= 1:
        ship_row2 = ship_row + 1
        ship_row3 = ship_row + 2
    else:
        ship_row2 = ship_row - 1
        ship_row3 = ship_row - 2

    #The next 3 lines tell the user the answer, useful only for debugging:
    #print "rrrc"
    #print ship_row
    #print ship_row2
    #print ship_row3
    #print ship_col

if row_or_col == 1:
    if ship_col <= 1:
        ship_col2 = ship_col + 1
        ship_col3 = ship_col + 2
    else:
        ship_col2 = ship_col - 1
        ship_col3 = ship_col - 2

    #The next 3 lines tell the user the answer, useful only for debugging:
    #print "cccr"
    #print ship_col
    #print ship_col2
    #print ship_col3
    #print ship_row

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!

hits = 0

for turn in range(7):
    print "\nTurn", turn + 1
    guess_row = int(raw_input("Guess Row (1-5):"))
    guess_col = int(raw_input("Guess Col (1-5):"))
    
    guess_row -=1
    guess_col -=1

    if row_or_col == 0:
        if (guess_row == ship_row or guess_row == ship_row2 or guess_row == ship_row3) and guess_col == ship_col:
            print "Congratulations! A hit."
            board[guess_row][guess_col] = "H"
            hits += 1
            if hits == 3:
                print "YOU SANK MY BATTLESHIP!"
                break
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print "\nOops, that's not even in the ocean.\n"
                if turn == 6:
                    print "Game Over\n"
            elif(board[guess_row][guess_col] == "X"):
                print "\nYou guessed that one already.\n"
                if turn == 6:
                    print "Game Over\n"
            else:
                print "\nYou missed my battleship!\n"
                board[guess_row][guess_col] = "X"
                if turn == 6:
                    print "Game Over\n"
    else:
        if (guess_col == ship_col or guess_col == ship_col2 or guess_col == ship_col3) and guess_row == ship_row:
            print "Congratulations! A hit."
            board[guess_row][guess_col] = "H"
            hits += 1
            if hits == 3:
                print "YOU SANK MY BATTLESHIP!"
                break
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print "\nOops, that's not even in the ocean.\n"
                if turn == 6:
                    print "Game Over\n"
            elif(board[guess_row][guess_col] == "X"):
                print "\nYou guessed that one already.\n"
                if turn == 6:
                    print "Game Over\n"
            else:
                print "\nYou missed my battleship!\n"
                board[guess_row][guess_col] = "X"
                if turn == 6:
                    print "Game Over\n"
        
    # Print (turn + 1) here!
    print "A summary of your guesses: "
    print_board(board)
