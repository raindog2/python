print "What file would you like to write 'hoochy' to?"
filename = raw_input("> ")

txt = open(filename)

print "Writing 'hoochy' to %r:" % filename
txt.write("hoochy") 



