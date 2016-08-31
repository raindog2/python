# Name: Mark Purcell
# Date: June 5, 2015

import random

user = raw_input("\nChoose: \nrock\npaper\nscissors\nlizard\nspock\n\n")
comp = random.choice( ['rock','paper','scissors','lizard','spock'] )

print '\nyour choice:', user
print 'my choice:', comp

if user == comp:
    print 'TIE!'
elif (user == 'paper' and (comp == 'rock' or comp == 'spock')) or (user == 'rock' and (comp == 'scissors' or comp == 'lizard')) or (user == 'scissors' and (comp == 'paper' or comp == 'lizard')) or (user == 'lizard' and (comp == 'paper' or comp == 'spock')) or (user == 'spock' and (comp == 'rock' or comp == 'scissors')):
    print 'YOU WIN!'
else: print 'I WIN!'
