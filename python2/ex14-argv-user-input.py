from sys import argv

script, user_name, food, color = argv
prompt = '> '

print "\nHi %s, my name is \"%s\"." % (user_name, script)

print "\nI'd like to ask you a few questions. Is that OK?"
raw_input(prompt)

print "\nFirst question, do you like %s?" % food
likes = raw_input(prompt)

print "\nAnd so where do you live, %s?" % user_name
lives = raw_input(prompt)

print "\nAaaand, who's your favorite Sounder?"
sounder = raw_input(prompt)

print "\nLast question, most important: what is your opinion of the color %s?" % color
opinion = raw_input(prompt)

print """
Alright, so to recap, you said %r about liking %s.
You live in %r. Not sure where that is, but I bet it's nice.
Your favorite Sounder is %s. Nice.
And your opinion of the color %s is: %r. 
""" % (likes, food, lives, sounder, color, opinion)



