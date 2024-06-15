"""

How to Reverse a String in Python

There is no built-in function to reverse a String in Python.

The fastest (and easiest?) way is to use a slice that steps backwards, -1.

"""

txt = "Hello World"[::-1]
print(txt)

# Function

def my_function(x):
  return x[::-1]

mytxt = my_function("I wonder how this text looks like backwards")

print(mytxt)

# Using a for loop

def reverse_string(input_string):
    # Initialize an empty string to store the reversed string
    reversed_string = ""
    # Loop through the input string in reverse order
    for i in input_string:
        # Prepend each character to the reversed_string
        reversed_string = i + reversed_string
    return reversed_string

# Example usage
original_string = "Hello, World!"
reversed_string = reverse_string(original_string)
print("Original string:", original_string)
print("Reversed string:", reversed_string)


