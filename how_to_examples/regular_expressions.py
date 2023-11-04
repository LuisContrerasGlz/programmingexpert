"""

A regular expression is a sequence of characters that defines a search pattern. Regular expressions are often used to perform pattern matching with strings, or to search and replace parts of strings.

In Python, you can use the re module to work with regular expressions. The re module provides functions for searching for and matching regular expressions, as well as functions for replacing and splitting strings.

To use regular expressions in Python, you first need to import the re module. Then, you can use one of the following functions:

re.match(pattern, string): Attempts to match the pattern at the beginning of the string. If the match is successful, it returns a match object; otherwise, it returns None.
re.search(pattern, string): Searches for the pattern in the string. If the search is successful, it returns a match object; otherwise, it returns None.
re.findall(pattern, string): Returns a list of all non-overlapping matches in the string.
re.sub(pattern, replacement, string): Replaces all occurrences of the pattern in the string with the replacement string.


"""

import re

string = "The quick brown fox"

# Search for a pattern using the search() function
match = re.search(r"quick", string)
if match:
    print("Match found:", match.group())
else:
    print("Match not found")


"""

The search() function searches for the pattern in the string and returns a match object if the pattern is found. The group() method of the match object returns the matched string.

Regular expressions can include special characters, such as . (match any character), * (match zero or more occurrences), and + (match one or more occurrences). 

"""


string = "The quick brown fox"

# Use the . character to match any character
pattern = r"q.ick"
match = re.search(pattern, string)
if match:
    print("Match found:", match.group())
else:
    print("Match not found")
