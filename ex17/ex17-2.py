from sys import argv
from os.path import exists

script, first_file, second_file = argv

print "The name of the files are %s and %s" % (first_file, second_file)

# I'm going to read the first file.
look_file = open(first_file)
look1_file= look_file.read()

print "^^^ That is what's in the file"
print "The first file is %d bytes long" % len(first_file)

print "Now I will write the words in %r to %r" % (first_file, second_file)

write_file = open(second_file, 'w')
write_file.write(look1_file)

write_file.close()
look_file.close()
