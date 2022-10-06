"""
Write a program that asks the user to input their age and tells them if they're old enough to ride a roller coaster. 
The minimum age to ride the roller coaster in this question is 13
"""

age = float(input("How old are you? "))

if age < 13:
    print("You can't ride the roller coaster.")
else:
    print("You can ride the roller coaster!")