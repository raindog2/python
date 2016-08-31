s = open("</absolute/path/to/sourcefile>", "r+")
d = open("</absolute/path/to/destinationfile>", "w")
for line in s:
    d.write(str(line))
d.close()
s.close()

