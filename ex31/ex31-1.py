print """
You have a massive poop coming during
a very expensive and important business meeting.

What do you do?
1) Leave the meeting and releave yourself.
2) Hold it in
3) Poop your pants and hope nobody notices.
"""

decision = raw_input("> ")

if decision == "1":
    print """
    After you left, they called your name to present.
    Your boss runs into the restroom and informs you
    that you have 1 minute before the investors leave.
    What do you do?
    1) Pinch it off and wipe your ass
    2) Push it out and don't wipe
    """
    choice = raw_input("> ")

    if choice == "1":
        print """
        You were able to present, but your poop made
        you cringe a couple times during the presentation.
        Investors were conserned.
        """
    elif choice == "2":
        print """
        Your presentation was very clear; however, you kept
        scratching your ass. Investors were pleased with
        your message, but not with your actions.
        """
    else:
        print "Choose '1' or '2'"

elif decision == "2":
    print """
    Because of the intense pressure of the situation,
    you kept farting during the presentation and all
    of the investors passed out.
    """
else:
    print """
    They noticed. You're fired.
    """
