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


"""

2. Write a program that continually asks the user to enter a word until they enter the word "q" or "quit"
   at which point the program should print the average length of all of the entered words, excluding the "q" or "quit"
   If the user doesn't enter any words (i.e., immediately enter "q" or "quit". Don´t print anything

"""

words = []

while True:
    word = input("Enter a word: ")

    if word == "q" or word == "quit":
        break

    words.append(word)

if len(words) > 0:
    word_length_sum = 0

    for word in words:
        word_length_sum += len(word)

    average_word_length = word_length_sum / len(words)
    print(f"The average word length is: {average_word_length}.")

"""

3. Use a while loop to print the squares of the numbers: 1, 3, 6, 10, 1 and 21

"""

nums = [1, 3, 6, 10, 15, 21]
idx = 0

while idx < len(nums):
    num = nums[idx]
    print(num ** 2)

    idx += 1