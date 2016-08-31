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


birthday = ["Happy birthday to you",
            "I don't want to get sued",
            "So I'll stop right there"]

happy_bday = Song(birthday)


ratm = ["They rally around the family",
        "With pockets full of shells"]

bulls_on_parade = Song(ratm)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

