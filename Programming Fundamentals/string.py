"""
1. Write a program that asks the user to input an integer.
   If the user inputs a valid integer, the program should ask them for their name, and it should convert their name to all uppercase letters before printing
   If the user doesn't input a valid integer, the program should capitalize whatever they entered and print it.

"""

from curses.ascii import isdigit

games = input("Enter an integer: ")

if games.isdigit():
    name = input("What is your name? ")
    print("Hello, " + name.upper())
else:
    print(games.capitalize())


