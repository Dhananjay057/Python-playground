"""
association - mapping meaning: belongs to, is one of the components, is part of something

Aggregation - combine, concatenate, accumulate - create a component object

Composition - same as aggregation with ONE CONDITION - the object that we assign cannot exist without the class to which this object is assigned to

Inheritance vs association - when to use which?

If object is PART of another object use association
If object is SUBTYPE of another object use inheritance

BankAccount HAS users - association
BankAccount has many types of bank accounts like MinimumBalanceAccount - inheritance

"""

class Rectangle:
    def __init__(self,length:float ,width:float):
        self.length = length
        self.width = width

    def surface_area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)

class Cuboid():
    def __init__(self,figure, height):
        self.figure = figure
        self.height = height

    def surface_area(self):
        return 2 * self.figure.surface_area() + 2 * self.height * (self.figure.length + self.figure.width)
    
    def volume(self):
        return self.figure.surface_area() * self.height

class Cube(Cuboid):
    def __init__(self,figure: Square):
        super().__init__(figure, figure.length)


rectangle = Rectangle(4, 5)
print("Surface area of rectangle:", rectangle.surface_area())
# square = Square(4)
# print("Surface area of square:", square.surface_area())
cube = Cuboid(Rectangle(4, 5), 4)
print("Volume of cube:", cube.volume())