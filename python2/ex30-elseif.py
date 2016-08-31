#people = 30
#cars = 40
#buses = 15

print "How many people?",
people = input()

print "How many cars?",
cars = input()

print "how many buses?",
buses = input()

if cars > people and buses <= 2:
    print "Since there are more cars than people and not many buses, we should take the cars."
elif cars < people and buses >=2:
    print "Since there are more people than cars, and ample buses, we should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "More buses than cars.  That's too many buses."
elif buses < cars:
    print "Fewer buses than cars: maybe we should take the buses."
else:
    print "Buses = cars. We still can't decide."

if people > buses:
    print "More people that buses: let's just take the buses."
else:
    print "More buses than people?  Let's stay home then."
    
