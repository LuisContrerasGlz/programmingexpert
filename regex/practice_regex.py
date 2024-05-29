"""

A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.

Python has a built-in package called re, which can be used to work with Regular Expressions.

"""

# Search the string to see if it starts with "The" and ends with "Spain":

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

"""

RegEx Functions

Function	Description

findall	    Returns a list containing all matches
search	    Returns a Match object if there is a match anywhere in the string
split	    Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string

"""

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# Return an empty list if no match was found:
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

# Search for the first white-space character in the string:

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

# Make a search that returns no match:

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

# Split at each white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)


