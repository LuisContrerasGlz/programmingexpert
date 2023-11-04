"""

    Create a ContactInformation class that is instantiated by passing a first_name, last_name, email and phone_number.
    This class should store all of the passed values as instance attributes and have an additional attribute country that is set by default to None.

    After creating the class, instantiate two instances of it. 
    The first instance should be stored in the variable called person1 and person2

"""


class ContactInformation:
    def __init__(self, first_name, last_name, email, phone_number, country=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.country = country


person1 = ContactInformation(
    "Luis", "Contreras", "luis.fco.contreras@gmail.com", 449114564, "Mex")
person2 = ContactInformation(
    "Fernando", "Contreras", "luis.fer.contreras@gmail.com", 449114564, "Mex")
