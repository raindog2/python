from sys import argv

# sets up the inout file we are going to work with
script, input_file = argv

# defines the function print_all, which takes the argument f and prints the results of the command read, applied to f
def print_all(f):
    print f.read()

# defines the function rewind, which takes the argument f and issues the command seek, applied to f
def rewind(f):
    f.seek(0)

# defines the function print_a_line, which takes the arguments line_count and f, and prints the content of line_count and the results of the command readline, applied to f
def print_a_line(line_count, f):
    print line_count, f.readline()

# sets the variable current_file as = the output of running the command open on the original input file
current_file = open(input_file)

print "First let's print the whole file:\n"

# calls the function print_all with the argument current_file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#calls the function rewind with the argument current_file
rewind(current_file)

print "Let's print three lines:"

# sets the variable current_line as = 1
current_line = 1
#calls the function print_a_line with the arguments current_line and current_file)...print_a_line then defines its arugment line_count as = current_line (= 1) and defines current_file = f, on which it sicks the readline command
print_a_line(current_line, current_file)

# adds 1 to the definition of current_line, then calls print_a_line all over again
current_line = current_line + 1
print_a_line(current_line, current_file)

# adds 1 to the definition of current_line, then calls print_a_line all over again
current_line = current_line + 1
print_a_line(current_line, current_file)

