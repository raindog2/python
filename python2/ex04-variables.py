#sets the variable 'cars' to 100
cars = 100
#sets the variable
space_in_a_car = 4.0
#same
drivers = 30
#same
passengers = 90
#sets a variable value using the values of other variables
cars_not_driven = cars - drivers
#same as 9
cars_driven = drivers
#same as 9
carpool_capacity = cars_driven * space_in_a_car
#same as 9
average_passengers_per_car = passengers / cars_driven

#prints the output of the 'cars' variable 
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

