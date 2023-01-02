# Changing the position using assigment shorcut

first = input("Enter first number: ")
second = input("Enter second number: ")
print("Before swapping: ", first, second)

first, second = second, first

print("After swapping: ", first, second)