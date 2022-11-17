"""

    Write a program that asks the user to enter two integers representing the
    start and the end of a range. The program should then generate a random
    number within this range (inclusively) and ask the user to guess numbers
    until they guess the randomly generated number. Once the user guesses the
    random number, the program should tell them how many attempts it took them
    to guess it.

    Your program needs to ensure that the range of numbers given is valid. 
    For example, if the user enters a number for the end of the range that is less
    than the start of the range your program needs ask them to enter a valid
    number. 

    Note: You may assume the start of the range will never be negative (i.e you
    don't need to handle negative values).



"""


import random

inicio = input("Enter the start of the range: ")
# print(inicio)
while not inicio.isdigit():
    print('Please enter a valid number.')
    inicio = input('Enter the start of the range: ')
fin = input("Enter the end of the range: ")
while not fin.isdigit() or int(fin) < int(inicio):
    print('Please enter a valid number.')
    fin = input('Enter the end of the range: ')
# print(fin)


num_aleatorio = random.randint(int(inicio), int(fin))
# print(num_aleatorio)

adivino = int(input("Guess a number: "))

contador_intentos = 1

while adivino != num_aleatorio:
    adivino = int(input("Guess a number: "))
    contador_intentos += 1

print(f"You guessed the number in {contador_intentos} attempts")

    
    
    