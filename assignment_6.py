"""
Create a class called Shape.
Define a method in it called what_am_i
that prints "I am a shape" when called.
Change your Square and Rectangle classes
from the previous challenges to inherit from Shape,
create Square and Rectangle objects,
and call the new method on both of them.
"""

class Shape():
    def __init__(self, l, w):
        self.len = l
        self.width = w

    def what_am_i(self):
        print("I am a shape")

class Square(Shape):
    pass

class Rectangle(Shape):
    pass

a_square = Square(20, 20)
a_square.what_am_i()
a_rectangle = Rectangle (10, 5)
a_rectangle.what_am_i()
