	name = 'Mark Purcell'
age = 42 #not a lie
height = 73 # inches
height_cm = height * 2.5
weight = 192 # lbs
weight_kg = weight * 0.45
eyes = 'brown'
teeth = 'white'
hair = 'no'

print "Let's talk about %s." % name
print "He's %s cm tall." % height_cm
print "He's %r kg heavy." % weight_kg
print "That's %s in pounds, if you prefer imperial!" % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height_cm, weight, age + height_cm + weight) 
