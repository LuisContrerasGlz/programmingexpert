# Print the second item in the fruits list.

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

# Change the value from "apple" to "kiwi", in the fruits list.

fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"


# Use the append method to add "orange" to the fruits list.

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

# Use the insert method to add "lemon" as the second item in the fruits list.

fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")

# Use the remove method to remove "banana" from the fruits list.

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

# Use negative indexing to print the last item in the list.

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

# Use a range of indexes to print the third, fourth, and fifth item in the list.

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

# Use the correct syntax to print the number of items in the list.

fruits = ["apple", "banana", "cherry"]
print(len(fruits))

# Change a list to string


"""
Concatenate Elements with a Separator

The most common way to convert a list to a string is to use the str.join() method, which concatenates elements of the list with a specified separator. 
This method is generally used when you want a human-readable format, such as joining words to form a sentence.

"""

# Given a list of words
words = ["Hello", "world", "this", "is", "Python"]

# Join the words into a single string with a space separator
result = " ".join(words)
print(result)  # Output: "Hello world this is Python"

# Join with a comma separator
result = ", ".join(words)
print(result)  # Output: "Hello, world, this, is, Python"


