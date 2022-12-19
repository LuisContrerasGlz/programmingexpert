"""
Create an Animan, Mamal and Reptile class as defined below. 
Then create a Monkey and Lizard class that inherit from the proper base classes.

All Mammals and Reptiles are Animals; your inheritance should reflect this.
All Animals have an age weight and height. All Mammals have a sex and most Reptiles have 4 legs but no all.  Your classes should represent this.

All Monkeys have exactly 5 fingers and a color.
All Lizards have a tail and also have a color
Your classes should represent this.

"""

class Animal:
    def __init__(self, age, weight, height):
        self.age = age
        self.weight = weight
        self.height = height


class Mammal(Animal):
    def __init__(self, age, weight, height, sex):
        super().__init__(age, weight, height)
        self.sex = sex


class Reptile(Animal):
    def __init__(self, age, weight, height, legs):
        super().__init__(age, weight, height)
        self.legs = legs


class Monkey(Mammal):
    fingers = 5

    def __init__(self, age, weight, height, sex, color):
        super().__init__(age, weight, height, sex)
        self.color = color


class Lizard(Reptile):
    tail = True

    def __init__(self, age, weight, height, legs, color):
        super().__init__(age, weight, height, legs)
        self.color = color
