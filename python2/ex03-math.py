print "I will now count my chickens:"

print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
#3+2=5, +1=6, -5=1, +4%2(which is 0)=1, -1/4=1 (because the 1/4 is treated as 0.25=0), +6=7  

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

# Help with the floating point stuff:
>>> 1000.0 / 11  # quotient
90.9090909090909 # since 1000 has a .0 on it, it keeps the decimal
>>> 1000 / 11  # "floored" quotient
90  #since 1000 has no .0, it drops the decimal
>>> 1000 % 11  # remainder (this means: the remainder when you divide 1000/11 and drop the decimal)
10
#other examples of %:
100 % 60 = 40
100.0 % 60 = 40 # doesn't change it
10 % 4 = 2
500 % 3000 = 500 # because 500/3000=0
>>> 90 * 11 + 10  # control, should be 1000
1000
