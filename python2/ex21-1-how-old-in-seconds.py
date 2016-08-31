prompt = "> "

def seconds_in_hour(seconds):
    return seconds * 60
    
def seconds_in_day(seconds_in_hour):
    return seconds_in_hour * 24

def seconds_in_year(seconds_in_day):
    return seconds_in_day * 365

def age_in_seconds(seconds_in_year):
    return seconds_in_year * age
       
print "\nWelcome to the Python machine for discovering how old you are in seconds!\n"

print "Let's start with an easy one: what's your name?"
name = raw_input(prompt) 

print "\nAaaand another easy one: how many seconds in a minute?"
seconds = input(prompt)

print "\nSo that makes", seconds_in_hour(seconds), "seconds in an hour. Easy."
#seconds_in_hour_output = seconds_in_hour(seconds)

print "\nHmmm, OK...if there are", seconds_in_hour(seconds), "seconds in an hour, that would be", seconds_in_day(seconds_in_hour(seconds)), "seconds in a day, right?"
raw_input(prompt)

#seconds_in_day_output = seconds_in_day(seconds_in_hour_output)

print "\nWhich would then mean there are", seconds_in_year(seconds_in_day(seconds_in_hour(seconds))), "seconds in a year. (Geez that's a lot). But with me so far?"
raw_input(prompt)

print "\nOK...so, big question: how old are you in years? (You can approximate, but you can also use decimals...)"
age = input(prompt)

#seconds_in_year_output = seconds_in_year(seconds_in_day_output)

print "\nOuch. OK, well, be that as it may, if you are", age, "years old, then that means you are %s *" % (age), seconds_in_year(seconds_in_day(seconds_in_hour(seconds))), "seconds old, which is...(big reveal)\n\n", age_in_seconds(seconds_in_year(seconds_in_day(seconds_in_hour(seconds)))), "seconds old!!!\n\nDon't worry %s, everything is going to be fine.\n" % (name)


