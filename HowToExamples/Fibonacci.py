"""

A Fibonacci series is a sequence of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. For example, the first few numbers in the Fibonacci series are:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The Fibonacci series can be defined recursively as follows:

The first two numbers in the series are 0 and 1.
Each subsequent number in the series is the sum of the previous two numbers.
Therefore, the nth number in the series is the sum of the (n-1)th and (n-2)th numbers.
"""

def fibonacci(n):
  # Set the initial values of the series
  a, b = 0, 1

  # Initialize an empty list to store the series
  series = []

  # Generate the series
  while b < n:
    # Append the next number in the series to the list
    series.append(b)
    # Calculate the next number in the series
    a, b = b, a + b

  return series

# Test the function
print(fibonacci(10))
# Output: [1, 1, 2, 3, 5, 8]
print(fibonacci(20))
# Output: [1, 1, 2, 3, 5, 8, 13]
