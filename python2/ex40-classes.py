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

# NB: written in python2

class Song(object):

    def __init__(self, artist, title, lyrics):
        self.artist = artist
        self.title = title
        self.lyrics = lyrics

    def info(self):
        print "\nARTIST: ", self.artist
        print "TITLE: ", self.title

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday_lyrics = ["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"]
happy_bday = Song("Some Guy", "Happy Birthday", happy_bday_lyrics)

long_way_lyrics = ["Money's just something you throw", "Off the back of a train", "Got a head full of lightning", "A hat full of rain"]
long_way = Song("Tom Waits", "Long Way Home", long_way_lyrics)

hold_on_lyrics = ["How I miss your broken China voice", "How I wish you were still here with me"]
hold_on = Song("Tom Waits", "Hold On", hold_on_lyrics)

bulls_on_parade_lyrics = ["They rally around the family", "With a pocket full of shells"]
bulls_on_parade = Song("Rage Against the Machine", "Bulls on Parade", bulls_on_parade_lyrics)

happy_bday.info()
happy_bday.sing_me_a_song()
print
long_way.info()
long_way.sing_me_a_song()
print
hold_on.info()
hold_on.sing_me_a_song()
print
bulls_on_parade.info()
bulls_on_parade.sing_me_a_song()

