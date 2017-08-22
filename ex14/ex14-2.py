from sys import argv

user_name, input1, input2, input3 = argv
prompt = '-->'

print """
The script name is %s, the first input is %s
the second input is %s, and the third input is %s.
""" % (user_name, input1, input2, input3)

print "There will be a list of questions given to you."

print "Is the name of this script %s?" % user_name
script_name = raw_input(prompt)

print "What was the second input?"
second_input = raw_input(prompt)

print "What was the first input?"
first_input = raw_input(prompt)

print """
You are correct if you said the script name is ex14-2.py.
You said the name was %s. Good Job. Or was it?
The second input according to you was %s.
The first input according to you was %s.
""" % (script_name, second_input, first_input)
