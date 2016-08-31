#Symbols

'   encloses a stri'
"   encloses a string "
''' encloses a string that is on multiple lines '''
""" encloses a string that is on multiple lines """
#   marks a comment
=   sets a value for a variable
,   separates two things, e.g. a string from a variable name
+   adds two numbers
-   subtracts two numbers
*   multiplies two numbers
/   divides two numbers
>   greater than
>=  greater than or equal to
<   less than
<=  less than or equal to
%   1000 % 11 returns the remainder when you divide 1000/11 and drop the decimal from the result
%   also serves to mark an embedded variable, as in "%d mi is how far to go", % (miles)
%d  an embedded variable that returns an integer
%s  an embedded variable that returns a string
%r  an embedded variable that returns raw data
\   escapes one character from a string
\n  new line
\t  tab space
\"  "to actually print quotes in some output
\\  if you want to print the actual backslash

#Commands

print   prints a line
#To get user input
print "How old are you?"
raw_input() 
#for user-provided input of any form, or
input() 
#for user-provided integer input, or all on one line:
age = raw_input("How old are you? ") 
age = input("How old are you? ")

from sys import argv    #imports command argv, which sets up variables given by user at the beginning of the program, in the same command in which the script is invoked 
script, first, second, third = argv #unpacks argv into four variables

#working with files
txt = open(filename) #defines txt as the result of opening a given file
txt = open(filename, 'w') #defines txt as the result of opening a given file for writing to--truncates (erases) the file [ex16]
txt = open(filename, 'r') #defines txt as the result of opening a given file for reading [ex16]
txt = open(filename, 'a') #defines txt as the result of opening a given file for appending text
txt.truncate() #erases the file you opened with open
txt.truncate() #erases the file you opened with open
txt.close() #closes the file	
print txt.read() #shoves the open content of filename (txt) through the command read with no options: (), then prints the result
also: txt.write("string" or variable value) #writes "string" or variable value into the file you opened using the "w" option [ex15,16]
