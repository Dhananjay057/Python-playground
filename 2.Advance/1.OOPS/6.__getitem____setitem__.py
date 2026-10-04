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

class Rocketboard:
    def __init__(self):
        self.rockets = [Rocket(randint(1,6)) for __ in range(10)]

        for __ in range(10):
            rocketIndexTomove = randint(0,len(self.rockets)-1)
            self.rockets[rocketIndexTomove].move_up()

        for rocket in self.rockets:
            print(rocket)

    def __getitem__(self, key):
        return key





"""__getitem__() and __setitem__() are dunder methods in Python. 
They allow us to control how a custom object behaves when we use square brackets [] to access or modify data.

1. __getitem__()

__getitem__() is called when we get, access, or read a value from an object using [].

Example:
class Student:
    def __init__(self):
        self.data = {
            "name": "Dhananjay",
            "age": 25
        }

    def __getitem__(self, key):
        return self.data[key]


student = Student()

print(student["name"])
print(student["age"])

Output:

Dhananjay
25

When we write:

student["name"]

Python internally calls:

student.__getitem__("name")

So:

__getitem__() → controls how values are retrieved using [].

2. __setitem__()

__setitem__() is called when we set, change, or update a value using [].

Example:
class Student:
    def __init__(self):
        self.data = {
            "name": "Dhananjay",
            "age": 25
        }

    def __setitem__(self, key, value):
        self.data[key] = value


student = Student()

student["age"] = 26

print(student["age"])

Output:

26

When we write:

student["age"] = 26

Python internally calls:

student.__setitem__("age", 26)

So:

__setitem__() → controls how values are assigned or updated using []."""