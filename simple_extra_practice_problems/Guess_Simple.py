"""


The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!

Here is a transcript of an example session:

Please think of a number between 0 and 100!
Is your secret number 50?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 75?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 87?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 81?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 84?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 82?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 83?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
Game over. Your secret number was: 83

Hint: Endpoints

** Your program should use bisection search. So think carefully what that means. What will the first guess always be? How should you calculate subsequent guesses?

** Your initial endpoints should be 0 and 100. Do not optimize your subsequent endpoints by making them be the halfway point plus or minus 1. Rather, just make them be the halfway point.

Python Trick: Printing on the same line

Try the following in your console:

# Notice how if we have two print statements                
print("Hi")
print("there")

# The output will have each string on a separate line:                
Hi
there
                
# Now try adding the following:
print("Hi",end='')
print("there")
print("Hi",end='*')
print("there")   
                
# The output will place the subsequent string on the same line
# and will connect the two prints with the character given by end
Hithere
Hi*there                
         
Note: your program should use input to obtain the user's input! Be sure to handle the case when the user's input is not one of h, l, or c.

When the user enters something invalid, you should print out a message to the user explaining you did not understand their input. Then, you should re-ask the question, and prompt again for input.

"""

print("Please think of a number between 0 and 100!")

low = 0
high = 100
ans = (high + low)//2

while True:
    print("Is your secret number " + str(ans) + "?")
    user_input = input(
        "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if user_input == 'c':
        print("Game over. Your secret number was: " + str(ans))
        break
    elif user_input == 'h':
        high = ans
    elif user_input == 'l':
        low = ans
    else:
        print("Sorry, I did not understand your input.")
    ans = (high + low)//2
