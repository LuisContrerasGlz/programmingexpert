"""

Create an abstract Animal class that contains the following methods:

sleep(): , a concrete method that outputs "ZzzZzz" to the console
animal_sound(), an abstract method that raises a NotImplementedError if called.
wake_up(),  a concrete method that calls animal_sound() and outputs "I am awake!" to the console

After creating the Animal class create a subclass named Lion that implements the Animal class.
When animal_sound() is called on an instance of the "Lion" class it should output "Roar!"

"""


class Animal:
    def sleep(self):
        print("ZzzZzz")

    def animal_sound(self):
        raise NotImplementedError("Method not implemented.")

    def wake_up(self):
        self.animal_sound()
        print("I am awake!")


class Lion(Animal):
    def animal_sound(self):
        print("Roar!")
