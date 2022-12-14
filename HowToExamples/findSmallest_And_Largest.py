# Find the smallest and largest element in a list
numbers = [3, 7, 2, 8, 4]
smallest = min(numbers)
largest = max(numbers)

print(f"Smallest number: {smallest}")
print(f"Largest number: {largest}")

# Using min() and max() functions with a key argument to specify a function that returns the value that should be used for comparison.

# Find the smallest and largest string in a list based on length
words = ["cat", "window", "defenestrate"]
shortest = min(words, key=len)
longest = max(words, key=len)

print(f"Shortest word: {shortest}")
print(f"Longest word: {longest}")

"""

To find the second smallest and second largest elements in a list in Python, 
we can use the sorted() function to sort the list, 
and then use indexing to get the second smallest and second largest elements.

"""

# Find the second smallest and second largest element in a list
numbers = [3, 7, 2, 8, 4]
sorted_numbers = sorted(numbers)

second_smallest = sorted_numbers[1]
second_largest = sorted_numbers[-2]

print(f"Second smallest number: {second_smallest}")
print(f"Second largest number: {second_largest}")

# We can also use the min() and max() functions with a key argument to specify a function that returns the value that should be used for comparison.

# Find the second smallest and second largest string in a list based on length
words = ["cat", "window", "defenestrate"]
sorted_words = sorted(words, key=len)

second_shortest = sorted_words[1]
second_longest = sorted_words[-2]

print(f"Second shortest word: {second_shortest}")
print(f"Second longest word: {second_longest}")

# Other way with for

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print(largest)
