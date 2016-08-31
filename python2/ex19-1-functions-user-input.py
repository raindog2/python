# Defines the function (cheese_and_crackers) 
# as having two arguments (cheese_count, boxes...) and printing a
# few lines based on those variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %s cheeses!" % cheese_count
    print "You have %s boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# gets user input to define the variables
# raw input is treated as a string (%s) 
# in the function above
amount_of_cheese = raw_input("\nHow many cheeses do you have? ")
amount_of_crackers = raw_input("\nAaaaand, how many boxes of crackers? ")

# calls the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


