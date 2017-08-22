from sys import exit

class Racing(Scene):

    def enter(self):
        print"""
        This is formula One. You are in second place
        on the final lap of the race and you have
        three corners left to overtake. Which corner
        do you want to overtake on?
        '1, 2, or 3' """

        corner_chosen = int(raw_input('> '))

        if corner_chosen == 1:
            print """
            The turn was too tight. You understeered into
            first place and both of you crashed. There
            will be a fight as soon as he gets out of the car.
            Well done."""

        elif corner_chosen == 2:
            print """
            You are able to nudge your nose into the corner.
            You have taken the inside lane and will win as
            long as you keep your composure. However, you have
            to pee really bad. What do you do?
            'Pee' to keep your cool? or 'no pee' and lose the race."""

            pee_chosen = raw_input('> ')

            if pee_chosen == 'pee' or 'Pee':
                print "Nice, you win."

            elif pee_chosen == 'no pee' or 'don\'t pee':
                print "Sorry you lost."

            else:
                print "Please type 'pee' or 'no pee'"

        elif corner_chosen == 3:
            print """
            Your opponent kept his cool and closed you out,
            better luck next time. And remember... If you
            ain't first, you're last."""

        else:
            print "Please type the number 1 , 2 , or 3."

    def V8SuperCar(self):
        print"""
        You've got the race in the bag. Congrats. I don't
        have the time or energy to make a game out of This
        one."""

    def Nascar(self):
        print """
        Great!! You're turning left! Hard stuff. Do you think
        you're good enough to win? Yes or No """

        choice = raw_input('> ')

        if choice == 'Yes' or 'yes':
            print "Congrats, you're confident. You win"

        if choice == 'No' or 'no':
            print "If you believe you can't do something, you are right."

        else:
            print "Please type 'Yes' or 'No'"

class RunWar:
    pass


class Racing(Scene):

    def racing(self):
        print"""
        Choose from the following race games:
        -Formula One
        -V8 Supercar
        -Nascar
        """
        race_chosen = raw_input('> ')
        if race_chosen == 'Formula One' or 'formula one':
            r = Racing('Formula One')
            r.formulaOneGame()
        elif race_chosen == 'V8 Supercar' or 'V8 supercar' or 'v8 supercar':
            f = Racing('V8 Supercar')
            f.V8SuperCar
        elif race_chosen == 'Nascar' or 'nascar':
            r = Racing('Nascar')
            r.Nascar
        else:
            print "Please type one of the choices given"

class Map(object):

    scenes = {
    'Formula One' : formulaOneGame,
    'V8Supercar' : V8SuperCar,
    'Nascar' : Nascar,
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

M = Map('game')
M.intro()
