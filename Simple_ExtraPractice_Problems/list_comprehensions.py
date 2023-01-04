# Creating a list with numbers from 1 to 100 using list comprehensions

numbers = [i for i in range(1,101)]
print(numbers)

# Creating a list from 1 to 100 but skip the numbers that are divisible by 3

numbers3 = [i for i in range(1,101) if i % 3 != 0]
print(numbers3)

# Using list comprehensions to create a table with nested lists

table = [[i for i in range(1,6)] for j in range(4)]
print(table)