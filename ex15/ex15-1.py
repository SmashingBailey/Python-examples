from sys import argv

script, filename = argv

text = open(filename)

prompt = "> "

print "Here is your filename %r" % filename
print text.read()

print "Re-type the file name"
re_type = raw_input(prompt)

second_text = open(re_type)
print second_text.read()

print "I opened the file twice"
