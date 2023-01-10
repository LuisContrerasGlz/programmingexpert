# Creating a list with numbers from 1 to 100 using list comprehensions

numbers = [i for i in range(1, 101)]
print(numbers)

# Creating a list from 1 to 100 but skip the numbers that are divisible by 3

numbers3 = [i for i in range(1, 101) if i % 3 != 0]
print(numbers3)

# Using list comprehensions to create a table with nested lists

table = [[i for i in range(1, 6)] for j in range(4)]
print(table)

"""

List comprehension allows you to create new lists from existing ones in a concise and elegant way.
The syntax is [expression for element in list if conditional]

which is actually an equivalent of the following code:

for element in list:
    if conditional:
        expression

"""

cubed = [num ** 3 for num in range(5)]
print(cubed)  # outputs: [0, 1, 8, 27, 64]
