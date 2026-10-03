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
from math import sqrt

class Rocket:
    """
    represents the rocket that can move with set speed
    """
    
    def __init__(self,altitude: float=0, speed: float = 1, x: float =0):
        """
        keyword Arguments:
            speed {int} -- speed of rocket's engine - how fast the rocket flies (default: {1})
        """
        self.altitude = altitude
        self.x = x
        self.speed = speed

    def move_up(self):
        """
        it moves up the rocket by speed amount
        """
        self.altitude += self.speed

    def __str__(self):
        return "Current altitude of rocket is :"+ str(self.altitude)

    """ this feature provided to justb who runs rockets
     so we can move from here to rocketboard"""
    # def get_distance(self,rocket):
    #     ab = (rocket.altitude - self.altitude) **2
    #     bc = (rocket.x - self.x) **2
    #     return sqrt(ab + bc)


class Rocketboard:
    def __init__(self,amountOfRockets: int=5):
        self.rockets = [Rocket(randint(1,10)) for __ in range(amountOfRockets)]

        for __ in range(10):
            rocketIndexTomove = randint(0,len(self.rockets)-1)
            self.rockets[rocketIndexTomove].move_up()

        for rocket in self.rockets:
            print(rocket)

    def __getitem__(self, key):
        return self.rockets[key]

    """ @staticmethod removes the need of self parameter and 
    we can call this method without creating object of class"""

    @staticmethod 
    def get_distance(obj1: Rocket, obj2: Rocket) -> float: # all these annontations are optional but they help in understanding the code
        ab = (obj1.altitude - obj2.altitude) **2
        bc = (obj1.x - obj2.x) **2
        return sqrt(ab + bc)