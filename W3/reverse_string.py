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