from sys import argv
from os.path import exists

script, previous_file, new_file = argv

print "Copying from %s to %s" % (previous_file, new_file)

in_file = open(previous_file)
first_file = in_file.read()

print "The input file is %d bytes long" % len(first_file)
print "Does the output file already exist? %r" % exists(new_file)
print "Are you sure that you want to continue?"
raw_input("Hit RETURN to continue or CTRL-C to quit")

second_file = open(new_file, 'w')
second_file.write(first_file)

print "All right, done"

second_file.close()
in_file.close()

print "Now I will read the new file"

read_file = raw_input("What's the filename you just created?")
read1_file = open(read_file)

print read1_file.read()

print "Now I will close the file again"

read1_file.close()
