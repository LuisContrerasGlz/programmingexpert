# Changing the position using 3rd variable

first = input("Enter first number: ")
second = input("Enter second number: ")
print("Before swapping: ", first, second)

temporary = first
first = second
second = temporary

print("After swapping: ", first, second)