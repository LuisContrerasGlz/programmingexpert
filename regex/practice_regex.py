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

# Replace every white-space character with the number 9:

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# Replace the first 2 occurrences:

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

"""

A Match Object is an object containing information about the search and the result.

If there is no match, the value None will be returned, instead of the Match Object.

"""

# Do a search that will return a Match Object:

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object


