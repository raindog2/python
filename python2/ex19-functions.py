# defines the function (cheese_and_crackers) 
# as having arguments (cheese_count, boxes...) 
# and printing some lines
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# prints a line and then calls the function and defines the variables
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# prints a line and then defines the variables in a slightly different way and then calls the function
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# prints a line and then calls the function and defines the variables
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# prints a line and then calls the function and defines the variables
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


