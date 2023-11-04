"""

1. Write a program that asks the user to input their age and tells them if they're old enough to ride a roller coaster. 
   The minimum age to ride the roller coaster in this question is 13
   
"""

age = float(input("How old are you? "))

if age < 13:
    print("You can't ride the roller coaster.")
else:
    print("You can ride the roller coaster!")

"""

2. Write a program that asks the user to input their favorite programming
   language and outputs a specific string based on their answer.

"""

fav_language = input("What's your favorite programming language? ")

if fav_language == "Python":
    print("Nice choice!")
elif fav_language == "Golang":
    print("You're a cool kid I see...")
elif fav_language == "JavaScript":
    print("Okay Mr. web developer.")
else:
    print("I don't know that language.")
