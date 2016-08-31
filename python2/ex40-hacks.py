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

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line


#birthday = ["Happy birthday to you",
#            "I don't want to get sued",
#            "So I'll stop right there"]

#happy_bday = Song(birthday)


#ratm = ["They rally around the family",
#        "With pockets full of shells"]

name = raw_input("Hi, what's your name?\n")

print "Hi %s, please think of your favorite lyric that contains two lines...\n" % name

line1 = raw_input("Please type the first line...\n")
line2 = raw_input("OK, and please type the second line...\n")

user_lyric = [line1,
              line2]

user_song = Song(user_lyric)
print "\nThank you! So here is your lyric, in all its two-line glory:\n"
user_song.sing_me_a_song()

#bulls_on_parade = Song(ratm)

#happy_bday.sing_me_a_song()

#bulls_on_parade.sing_me_a_song()

