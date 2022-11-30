# Problem 1

class Rectangle:
    # Defining the contructor of the Rectangle
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # Defining a method to change the position of x and y with new values
    def change_position(self, x, y):
        self.x = x
        self.y = y

    # Defining get position method which returns x and y in a tuple 
    def get_position(self):
        return (self.x, self.y)

    # Defining the get area method which will use the width and height attributes to calculate and return the area
    def get_area(self):
        return self.width * self.height

