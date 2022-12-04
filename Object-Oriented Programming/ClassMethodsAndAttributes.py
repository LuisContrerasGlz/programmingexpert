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