# Remove unwanted characters from a string
s = "hello, world!"

s = s.replace(",", "")   # Remove ,
s = s.replace("!", "")   # Remove !

print(s)

# Remove unwanted characters from a string using regular expressions
import re

s = "hello, world!"

# Use the sub() function to remove all punctuation from the string
s = re.sub(r'[^\w\s]', '', s)

print(s)
