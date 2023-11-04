"""

    Write a program that asks a user for two numbers: a numerator and a denominator. 
    Your program should divide the numerator by the denominator and handle any exceptions that might occur during the division.

    Specifically, your program should catch exceptions when either the numerator or the denominator isn't a number 
    and when the denominator is 0.
    All exceptions should be caught and handled, even when there are multiple.

    If the division doesn't raise any exceptions, the program should print the result of the division. 
    And regardless of outcome, the program should tell the user goodbye!

"""

numerador = input("Enter the numerator: ")
denominador = input("Enter the denominator: ")

try:
    numerador = float(numerador)
except Exception as e:
    print("The numerator is not a number.")

try:
    denominador = float(denominador)
except Exception as e:
    print("The denominator is not a number.")

try:
    resultado = numerador / denominador
    print(f"The result of this division is {resultado}.")
except ZeroDivisionError:
    print("You cannot divide by 0.")
    print("This division cannot be performed.")
except Exception as e:
    print("This division cannot be performed.")
finally:
    print("Goodbye!")
