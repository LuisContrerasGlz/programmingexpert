"""

Write a function named get_longest_word which accepts a single string argument.
The function should return the longest word in the given string. Assume that words
in a string can be separated with spaces, commas, new line characters or full
stops. This means that abbreviated forms with apostrophes (e.g.I&#39;m) are
considered to be a single word. If there is more than one word with the maximum
number of characters, return the first such word that exists in the string.
Example: For input Once I&#39;m awaken, I&#39;ll sacrifice your soul to the ruler
of darkness. the output should be sacrifice.

"""


"""

sample_story = '''Once upon a time, there was a beginner programmer named Alice who was eager to learn Python. She tried to learn from books, but found it difficult to grasp the concepts. One day, she stumbled upon an online course.

Alice was thrilled. The course was taught by a well-known programmer who made the lessons interesting and easy to understand. The course covered everything a beginner programmer needed, and Alice was finally able to understand how to code in Python.'''


"""
# Option 1

def get_longest_word(input_string):
    words = words = input_string.replace('.', ' ').replace(',', ' ').split()
    longest_word = max(words, key=len)
    return longest_word

# Option 2

def get_longest_word2(input_string):

    words2 = input_string.replace('.', ' ').replace(',', ' ').split()
    temp_max_word2 = ''

    for word in words2:
        if len(word) > len(temp_max_word2):
            temp_max_word2 = word
    
    return temp_max_word2
