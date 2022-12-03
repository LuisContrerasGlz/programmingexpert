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

# Problem 2

class Group:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    # Declaring a method add to add a member to the members list using append
    def add(self, name):
        self.members.append(name)

    # Declaring the delete method to check if a name if already in members, if it is there we remove it with the .remove but if it is not there we raise an exception
    def delete(self, name):
        if name in self.members:
            self.members.remove(name)
        else:
            raise Exception("Member not in group.")

    # Declaring a get members function to return the order members, we use sorted() so we dont modify the original one, instead getting a new one
    def get_members(self):
        return sorted(self.members)


# Problem 3

class Group:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add(self, name):
        self.members.append(name)

    def delete(self, name):
        if name in self.members:
            self.members.remove(name)
        else:
            raise Exception("Member not in group.")

    def get_members(self):
        return sorted(self.members)

    def merge(self, group):
        combined_members = self.members + group.members
        new_group = Group("Any Name", combined_members)
        return new_group

# Problem 4

class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0.0

    # Def getter and returning the rounded of balance
    def get_balance(self):
        return round(self._balance)

    # Def the setter method checking the correct range of our checks
    def set_balance(self, balance):

        # Checking if it is a number
        if type(balance) not in [int, float]:
            return

        # Checking the range
        if balance < 0 or balance >= 100000:
            return

        # If all the conditions are good we have selt._balance been what was passed in there
        self._balance = balance

# Problem 5 

class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0.0

    @property
    def balance(self):
        return round(self._balance)

    @balance.setter
    def balance(self, balance):
        if type(balance) not in [int, float]:
            return

        if balance < 0 or balance > 100000:
            return

        self._balance = balance