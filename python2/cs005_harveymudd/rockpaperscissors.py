# Name: Mark Purcell
# Date: June 3, 2015

import random

user = raw_input("Choose: \nrock (r)\npaper (p)\nscissors (s)\n")
#comp = random.choice( ['r','p','s'] )
if user == 'r': comp = 'p'
elif user == 'p': comp = 's'
else: comp = 'r'

print 'your choice:', user
print 'my choice:', comp
#print 'I WIN'

if user == comp:
    print 'TIE!'
elif (user == 'p' and comp == 'r') or (user == 's' and comp == 'p') or (user == 'r' and comp == 's'):
    print 'YOU WIN!'
else: print 'I WIN!'
