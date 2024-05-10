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

