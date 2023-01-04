# Find the smallest and largest in a list

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
