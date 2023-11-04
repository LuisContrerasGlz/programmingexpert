"""

    Write a function that accepts a list of strings that represent words and a
    positive integer n , representing the number of words to return.
    Your function should return a new list containing the n longest unique words from the input list. 
    Words are unique if they only appear one time in the input list.

    There will always be exactly n words to return and you may
    return the words in any order.

    Note: all strings in the input list will not contain any special characters
    or spaces.

"""


def get_n_longest_unique_words(words, n):

    # Using the get_unique_words function to create the list from the parameter
    unique_words = get_unique_words(words)

    # We sort the words using the len, and reverse the order so it is correct in decending order
    sorted_words = sorted(unique_words, key=len, reverse=True)

    # We return a slice of the list up to n
    return sorted_words[:n]

# Defining a funtion to check the unique words of the list


def get_unique_words(words):
    # Declaring an empty list called unique words

    unique_words = []
    # Loopting the list and checking if the count of the words is 1, it it is we append it to the list

    for word in words:
        if words.count(word) == 1:
            unique_words.append(word)

    # We return the unique words
    return unique_words
