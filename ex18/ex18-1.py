# doing my first argument
def print_three(*args):
    arg1, arg2, arg3 = args
    print "This is arg1: %r, arg2: %r, and arg3: %r" % (
    arg1, arg2, arg3)

def print_two(arg1, arg2):
    print "This is arg1: %r, arg2: %r " % (arg1, arg2)

def print_one(arg1):
    print "This is arg1: %r" % arg1

def print_none():
    print "There's no print here"

print_three ("jacob", "devon", "eric")
print_two ("Ashley", "Mikayla")
print_one ("Bailey")
print_none ()
