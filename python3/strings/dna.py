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

from random import choice

def complement(dna):
    result = ""
    for c in dna:
        if c == "A":
            result += "T"
        elif c == "T":
            result += "A"
        elif c == "C":
            result += "G"
        elif c == "G":
            result += "C"
    return result

def is_dna(s):
    notinsequence = 0
    for c in s:
        if c not in "ATCG":
            notinsequence += 1
    if notinsequence > 0:
        return False
    else:
        return True

def is_rna(s):
    notinsequence = 0
    for c in s:
        if c not in "AUCG":
            notinsequence += 1
    if notinsequence > 0:
        return False
    else:
        return True
            
def reverse(dna):
    rev = ""
    for i in range(len(dna)):
        rev = dna[i] + rev 
    return rev

def reversecomp(dna):
    return reverse(complement(dna))
    #return complement(dna)[::-1]

def random_dna(length=30):
    fragment = ""
    for j in range(length):
        fragment += choice("ATCG")
    return fragment

def random_rna(length=30):
    fragment = ""
    for j in range(length):
        fragment += choice("AUCG")
    return fragment

def dna_transcription(dna):
    transcribed_dna = ""
    for c in dna:
        if c == "T":
            transcribed_dna += "U"
        else: 
            transcribed_dna += c
    return transcribed_dna

def is_palindrome(dna):
    if dna == reverse(dna):
        return True
    else:
        return False

def find_palidrome():
    dna = random_dna(10)
    while is_palindrome(dna) == False:
        print(dna)
        dna = random_dna(10)
    return dna

def countbases(dna):
    numA = 0
    numT = 0
    numC = 0
    numG = 0
    for c in dna:
        if c == "A":
            numA += 1
        elif c == "T":
            numT += 1
        elif c == "C":
            numC += 1
        elif c == "G":
            numG += 1
    counts = [numA, numT, numC, numG]
    return counts 

def main():
    # 12.3-4 Generate 10 DNA strings, their complements, and their reverse complements,
    # then test if they are RNA, then test if they are DNA, then transcribe 
    # the DNA into RNA
    print("Here is the DNA:\n")
    for i in range(10):
        dna = random_dna()
        print(dna + "     " + reversecomp(dna))
        print(complement(dna))
        print("Is RNA: " + str(is_rna(dna)))
        print("Is DNA: " + str(is_dna(dna)))
        print("Here is the transcribed RNA:\n" + dna_transcription(dna) + "\n")
    # 12.5-6 Generate 10 RNA strings, test if it is DNA, test if it is RNA
    print("Now for the RNA:\n")
    for i in range(10):
        rna = random_rna()
        print(rna)
        print("Is DNA: " + str(is_dna(rna)))
        print("Is RNA: " + str(is_rna(rna)) + "\n")
    # Randomly generate DNA strings until one is a palindrome
    print("Bonus: I found a DNA palindrome: " + find_palidrome())
    # 12.9 Generate a random DNA, then count how many of each nucleotide
    dna_to_count = random_dna()
    print(dna_to_count)
    print("As: " + str(countbases(dna_to_count)[0]))
    print("Ts: " + str(countbases(dna_to_count)[1]))
    print("Cs: " + str(countbases(dna_to_count)[2]))
    print("Gs: " + str(countbases(dna_to_count)[3]))
    #name = "aACGTACGTACGT"
    #print("Is " + name + " dna: " + str(is_dna(name.upper())))

main()
