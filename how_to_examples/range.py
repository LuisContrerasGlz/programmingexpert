"""

The range() function generates a sequence of numbers. It accepts integers and returns range objects. The syntax of range() looks as follows: range(start, stop, step), where:

start is an optional parameter specifying the starting number of the sequence (0 by default)
stop is an optional parameter specifying the end of the sequence generated (it is not included),
and step is an optional parameter specifying the difference between the numbers in the sequence (1 by default.)


"""

for i in range(3):
    print(i, end=" ")  # Outputs: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2
