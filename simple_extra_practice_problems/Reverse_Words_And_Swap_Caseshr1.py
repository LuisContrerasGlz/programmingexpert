"""

Implement a function that takes a string consisting of words separated by single spaces and returns a string containing all those words but in the reverse order and such that all cases of letters in the original string swapped

Function description:
The function has the following parameter(s):
string sentence: a given string of space-separated words
Returns: a string containing all the words from the sentence but in the reverse order and such that all cases of letters in the sentence string are swapped

Constrains:

sentence contains only English letters and spaces
sentence begins and ends with a letter
There are no 2 consecutive spaces in sentence
there are at most 10 words in sentence
the lengths of each of the words is at most 10

"""

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    # Split the sentence into a list of words
    words = sentence.split(" ")

    # Reverse the list of words
    words.reverse()

    # Join the reversed list of words into a single string
    reversed_sentence = " ".join(words)

    # Swap the cases of the reversed sentence
    swapped_sentence = reversed_sentence.swapcase()

    return swapped_sentence


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()
