# for codes refer rocket.py

"""

# @staticmethod

What is it?
@staticmethod is a decorator used to create a method inside a class.
* It does not use self or cls.
* It does not depend on object or class data.
* It can be called directly using the class name.

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

Calculator.add(10, 20)

When do we use it?
Use it when a function is related to a class but does not need any object or class information.
Commonly used for utility/helper functions.

Advantages :-
* No object creation required to call the method.
* Can avoid unnecessary memory usage from creating objects just to call a utility function.
* Keeps related functions organized inside the class.
* Makes it clear that the method doesn't depend on object/class state.

🧠 Memory Point

Static method = Class-related function that needs neither self nor cls.

self → Object
cls  → Class
none → Static

"""