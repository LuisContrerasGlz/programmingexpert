original_list = [1, 2, 3, 3, 4, 5, 5]

# Create a new set and add each element from the original list to it
no_duplicates = set()
for element in original_list:
    no_duplicates.add(element)

# Create a new list from the set
unique_list = list(no_duplicates)

print(unique_list)  # Output: [1, 2, 3, 4, 5]

# Using a list comprehension

unique_list = list(set(original_list))

print(unique_list)  # Output: [1, 2, 3, 4, 5]
