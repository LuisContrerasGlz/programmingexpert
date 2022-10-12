"""

1. Write a program that continually asks the user to enter a number until they enter the number 5,
   at which point the program should print how many numbers the user has entered.
   You may assume the user will only ever enter a number.

"""

number_entered = float(input("Enter a number: "))
counter = 0

while number_entered != 5:
    number_entered = float(input("Enter a number: "))
    counter += 1
print(f"You entered {counter+1} numbers.")