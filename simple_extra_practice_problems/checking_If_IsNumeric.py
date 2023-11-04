# Using the .isnumeric() string method

user_number = input("Please provide a number: ")

if user_number.isnumeric():
    print("Thank you, that is correct!")
else:
    print("Sorry, ", user_number, "is not a number")
