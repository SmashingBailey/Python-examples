from sys import argv

script, filename = argv

"The filename is %s" % filename
prompt = "> "
print "Type the filename again:"
print "You are about to delete %s." % filename
print "Do you want to continue? Hit CTRL-C if not"
print "To continue, hit RETURN"

raw_input("?")
print "Opening the file..."
target = open(filename, 'w')

target.truncate()
print "The file has been erased"



print """
These 3 lines will go into a file.
Write what you want to go into the file.
"""

print "First line: "
first = raw_input(prompt)
print "Second line:"
second = raw_input(prompt)
print "Third line:"
third = raw_input(prompt)

target.write(first)
target.write("\n")
target.write(second)
target.write("\n")
target.write(third)
target.write("\n")

print "Now we close it"
target.close()
