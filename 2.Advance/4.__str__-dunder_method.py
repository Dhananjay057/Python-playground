# dunder - Double Underscore
# __str__ - String

"""
_str__() 
__str__() is a dunder method in Python.
It defines the human-readable string representation of an object.
It is automatically called when using print(object) or str(object).
It must return a string.
It is useful for making objects easier to understand when printed.

Example:

def __str__(self):
    return self.name

So, print(student) will display the student's name instead of a default object address."""


from random import randint

class Rocket:
    """
    represents the rocket that can move with set speed
    """
    
    def __init__(self,speed=1):
        """
        keyword Arguments:
            speed {int} -- speed of rocket's engine - how fast the rocket flies (default: {1})
        """
        self.altitude = 0
        self.speed = speed

    def move_up(self):
        """
        it moves up the rocket by speed amount
        """
        self.altitude += self.speed

    def __str__(self):
        return "Current altitude of rocket is :"+ str(self.altitude)

rockets = [Rocket(randint(1,6)) for __ in range(10)]

# print(rockets)

for __ in range(10):
    rocketIndexTomove = randint(0,len(rockets)-1)
    rockets[rocketIndexTomove].move_up()

for rocket in rockets:
    print(rocket)