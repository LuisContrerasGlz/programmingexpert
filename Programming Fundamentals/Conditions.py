"""

1. w, x, y, z evaluates condition to true

"""

w = 1
x = 1
y = 3
z = 2

# `condition_` variables.
condition_1 = w < x + y
condition_2 = x == y - 2
condition_3 = z != 0
condition_4 = z + z == z * z
condition_5 = w > 0

# All of these should print `True`.
print(condition_1)
print(condition_2)
print(condition_3)
print(condition_4)
print(condition_5)

"""

2. w, x, y, z evaluates condition to true

"""

w = "Hello"
x = "hello"
y = "hello"
z = "d"

# `condition_` variables.
condition_1 = w != "a"
condition_2 = w < x
condition_3 = x == y
condition_4 = y == "hello"
condition_5 = z > "c"

# All of these should print `True`.
print(condition_1)
print(condition_2)
print(condition_3)
print(condition_4)
print(condition_5)

# Numbers game program

number1 = float(input("Enter a number: "))

if number1 >= 10 and number1 <= 20:
    number2 = float(input("Enter another number: "))
    sum_of_numbers = number1 + number2

    print("The sum of these two numbers is:", sum_of_numbers)

    if sum_of_numbers > 100:
        print("That is a large sum!")
