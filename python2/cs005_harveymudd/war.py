# Name: Mark Purcell
# Date: June 3, 2015

import random

user = raw_input("What is your name? ")
print 'Hello,',user,'. Ready to play War?'
readiness = raw_input('y/n ')

user_hand = [random.choice( [2,3,4,5,6,7,8,9,10,11,12,13,14] ) for i in range(26)]
comp_hand = [random.choice( [2,3,4,5,6,7,8,9,10,11,12,13,14] ) for i in range(26)]

if readiness == 'y' or readiness == 'Y': 
	print '\nOK! Dealing the cards...'
	print 'You and I will each start with',len(user_hand),'cards.\n'
        print 'Your hand:',user_hand
        print 'My hand:',comp_hand
        print '\n(FYI, 11=J, 12=Q, 13=K, and 14=A)\n'
else:
	print 'Fine. See you later'
	exit(0)

round_num = 1

def test_for_doneness(user_hand, comp_hand):
	if len(user_hand) == 0:
            print 'You are out of cards. I win the War!\n'
            exit(0)
	elif len(comp_hand) == 0:
            print 'I am out of cards. You win the War!\n'
            exit(0)

def recap(user_hand, comp_hand, round_num):
        print '\nRECAP:'
        print 'You have', len(user_hand), 'cards:\n',user_hand
        print 'I have', len(comp_hand),'cards:\n',comp_hand,'\n'
        raw_input('Press any key to continue\n')


def wargame(user_warplay, comp_warplay, user_hand, comp_hand):

        user_warchest = []
        while len(user_warchest) < 3:
            x = random.choice(user_hand)
            if x != user_warplay: user_warchest.append(x)

        comp_warchest = []
        while len(comp_warchest) < 3:
            y = random.choice(comp_hand)
            if y != comp_warplay: comp_warchest.append(y)

        print 'Tie! We will each put 3 cards face down and one up...\n' 
        print 'Your upcard:',user_warplay
        print 'My upcard:',comp_warplay

        if user_warplay > comp_warplay:
            print 'You win!'
            user_hand.append(comp_warplay)
            user_hand += comp_warchest
            for i in comp_warchest:
                comp_hand.remove(i)
            comp_hand.remove(comp_warplay)
            print 'You win my upcard and my warchest, which was',comp_warchest
        elif user_warplay < comp_warplay:
            print 'I win!'
            comp_hand.append(user_warplay)
            comp_hand += user_warchest
            for i in user_warchest:
                user_hand.remove(i)
            user_hand.remove(user_warplay)
            print 'I win your upcard and your warchest, which was:',user_warchest
        else:
            user_warplay = random.choice(user_hand)
            comp_warplay = random.choice(comp_hand)
            wargame(user_warplay, comp_warplay, user_hand, comp_hand)

def main(user_hand, comp_hand, round_num):
        while len(user_hand) > 0 and len(comp_hand) > 0:

            print '======= Round', round_num,'======='
    
            user_play = random.choice(user_hand)
            comp_play = random.choice(comp_hand)
    
            print 'You play a', user_play
            print 'I play a', comp_play
    
            if user_play > comp_play:
                print 'You Win!'
                user_hand.append(comp_play)
                comp_hand.remove(comp_play)
                test_for_doneness(user_hand, comp_hand)
            elif user_play < comp_play:
                print 'I Win!'
                user_hand.remove(user_play)
                comp_hand.append(user_play)
                test_for_doneness(user_hand, comp_hand)
            else:  
                user_warplay = random.choice(user_hand)
                comp_warplay = random.choice(comp_hand)
                wargame(user_warplay, comp_warplay, user_hand, comp_hand)
            
            round_num += 1
            recap(user_hand, comp_hand, round_num)

main(user_hand, comp_hand, round_num)
