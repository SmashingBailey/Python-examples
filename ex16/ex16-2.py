from sys import argv

script, filename = argv

print "The script name is %s and the file name is %s" % (script, filename)

print """
If you do not want to delete the file
press CTRL-C and it will exit.
If you do want to delete it, press RETURN.
"""

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "The file has been deleted"
target.truncate()

print "Now I'm going to create a new file."

print "I will ask you for three things."
print "These will go in the new file."
print "Write carefully"

love = raw_input("What do you love to do?")
job = raw_input("What is your job?")
salary = raw_input("What is your salary?")

target.write(love)
target.write('\n')
target.write(job)
target.write('\n')
target.write(salary)
target.write('\n')

print "Now I'm going to close the file"
target.close()

print """
If you want to read the file you just created,
enter the filename again here.
If not, hit CTRL-C
"""
# Here I am going to re-open the file I created
# Remember you have to open the file before you can read it.

read_filename = raw_input("What's the filename? > ")
new_target = open(read_filename)

print new_target.read()
