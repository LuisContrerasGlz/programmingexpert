# Use the len function to print the length of the string.

x = "Hello World"
print(len(x))

# Get the first character of the string txt.

txt = "Hello World"
x = txt[0]

# Get the characters from index 2 to index 4 (llo).

txt = "Hello World"
x = txt[2:5]

# Return the string without any whitespace at the beginning or the end.

txt = " Hello World "
x2 = txt.strip()
print(x2)

# return a string without any blank space in python

original_str = "Hello World! This is a test."
no_spaces_str = original_str.replace(" ", "")
print(no_spaces_str)  # Output: "HelloWorld!Thisisatest."

original_str = "Hello World! This is a test."
no_spaces_str = "".join(original_str.split())
print(no_spaces_str)  # Output: "HelloWorld!Thisisatest."

# Convert the value of txt to upper case.

txt = "Hello World"
txt = txt.upper()

# Convert the value of txt to lower case.

txt = "Hello World"
txt = txt.lower()

# Replace the character H with a J.

txt = "Hello World"
txt = txt.replace("H", "J")

# insert the correct syntax to add a placeholder for the age parameter.

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# Convert a string to a list

"""

Split a String by a Delimiter

The most common way to convert a string into a list is by using the str.split() method, which splits a string into a list based on a specified delimiter. 
The default delimiter is whitespace, but you can specify any character or string as the delimiter.

"""

# Example with space-separated words
sentence = "This is a test"

# Split into a list of words
words = sentence.split()  # Default is whitespace
print(words)  # Output: ["This", "is", "a", "test"]

# Example with a comma-separated string
csv_data = "1,2,3,4,5"

# Split by a comma
numbers = csv_data.split(",")
print(numbers)  # Output: ["1", "2", "3", "4", "5"]

