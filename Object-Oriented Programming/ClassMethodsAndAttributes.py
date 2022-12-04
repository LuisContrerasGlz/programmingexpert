# Problem 1 

class Person:
  population = 0

  def __init__(self, name, age):
      self.name = name
      self.age = age
      self.population = 1
      Person.population += 1

p1 = Person("Tim", 100)
p2 = Person("Clement", 54)

x = Person.population

# Problem 2

class Employee:

    # Defining our class attributes first as the best practice indicates

    number_of_employees = 0
    average_age = 0
    average_salary = 0

    # Defining the constructor taking self, name, age, and salary
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

        # Making total age and total salary with the computation bellow
        total_age = Employee.average_age * Employee.number_of_employees
        total_salary = Employee.average_salary * Employee.number_of_employees

        # Updating the Employee.average_age, average_Salary and at the end adding 1 each time to the number_of_employees
        Employee.average_age = (total_age + age) / (Employee.number_of_employees + 1)
        Employee.average_salary = (total_salary + salary) / (Employee.number_of_employees + 1)
        Employee.number_of_employees += 1

# Problem 3


class Temperature:
    min_temperature = 0
    max_temperature = 1000

    def __init__(self, kelvin):
        if kelvin > self.max_temperature or kelvin < self.min_temperature:
            raise Exception("Invalid temperature.")

        self.kelvin = kelvin

    @classmethod
    def update_min_temperature(cls, kelvin):
        if kelvin > cls.max_temperature:
            raise Exception("Invalid temperature.")

        cls.min_temperature = kelvin

    @classmethod
    def update_max_temperature(cls, kelvin):
        if kelvin < cls.min_temperature:
            raise Exception("Invalid temperature.")

        cls.max_temperature = kelvin