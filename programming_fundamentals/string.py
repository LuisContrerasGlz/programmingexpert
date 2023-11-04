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

"""

2. Write a program that asks the user to input two words and determines if the first word is contained in the second one.

"""


first_word = input("Enter a word: ")
second_word = input("Enter another word: ")

if first_word in second_word:
    print("The first word is contained in the second one")
else:
    print("The first word isn't contained in the second one")

"""

3. Write a program that asks the user to input a sentence and outputs how many words are in the sentence.
   Try using an f-string to embed the number of words in your output, and don't worry about singularization when there's only one word

"""


user_sentence = input("Enter a sentence: ")
word_count = user_sentence.split(" ")

print(f"There are {len(word_count)} words in this sentence")

"""

4. Write a program that uses a single print statement to output the following text:

      *
     ***
    *****
   *******
    *****
     ***
      *
"""

print("    *\n   ***\n  *****\n *******\n  *****\n   ***\n    *")
