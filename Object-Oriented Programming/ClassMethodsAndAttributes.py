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
    number_of_employees = 0
    average_age = 0
    average_salary = 0

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

        total_age = Employee.average_age * Employee.number_of_employees
        total_salary = Employee.average_salary * Employee.number_of_employees
        Employee.average_age = (total_age + age) / (Employee.number_of_employees + 1)
        Employee.average_salary = (total_salary + salary) / (Employee.number_of_employees + 1)
        Employee.number_of_employees += 1