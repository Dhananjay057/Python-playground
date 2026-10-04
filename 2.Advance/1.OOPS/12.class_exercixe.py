"""
Create three classes:
1) Rectangle
2) Square
3) Cube

a) Create constructors (__init__)
b) methods calculating the surface_area of a square, rectangle, cube
c) a method calculating the volume of the cube

Consider how you can use inheritance to do this so that you don't repeat the code
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

class Cube(Square):

    def surface_area(self):
        return 6 * super().surface_area()

    def volume(self):
        return super().surface_area() * self.length


rectangle = Rectangle(4, 5)
print("Surface area of rectangle:", rectangle.surface_area())
square = Square(4)
print("Surface area of square:", square.surface_area())
cube = Cube(4)
print("Volume of cube:", cube.volume())