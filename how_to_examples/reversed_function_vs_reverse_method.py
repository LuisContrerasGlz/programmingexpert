"""

The reversed function is a built-in function in Python that returns an iterator that produces the items of the input in reverse order. 
It can be used to reverse the elements of any sequence (such as a list, tuple, or string), as long as the sequence is a valid input for the reversed function.

"""

original_list = [1, 2, 3, 4, 5]
reversed_iterator = reversed(original_list)
reversed_list = list(reversed_iterator)
print(reversed_list)  # Output: [5, 4, 3, 2, 1]

"""

On the other hand, the reverse method is a method of Python's list class that reverses the elements of the list in place. It does not return a new list with the elements in reverse order; 
instead, it modifies the original list so that its elements are in reverse order.

"""

original_list = [1, 2, 3, 4, 5]
original_list.reverse()
print(original_list)  # Output: [5, 4, 3, 2, 1]

"""

In summary, the main difference between the reversed function and the reverse method 
is that the reversed function returns a new iterable with the elements in reverse order, 
while the reverse method modifies the original list in place.

"""
