"""

 1. Write a program that asks the user to input five strings and stores them in a list.
 
    Then, the program should ask the user to input three numbers in the range of 0 and 4 inclusive (these numbers will represent list indices).
 
    Finally, the program should use these numbers to access the three strings at the corresponding indices in the previously created list, concatenate them,
    and print out the resulting string.
    
"""

string1 = input("Enter a string: ")
string2 = input("Enter a string: ")
string3 = input("Enter a string: ")
string4 = input("Enter a string: ")
string5 = input("Enter a string: ")

strings = [string1, string2, string3, string4, string5]

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

final_string = strings[num1] + strings[num2] + strings[num3]
print(final_string)
