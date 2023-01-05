# Find duplicates in a string

def find_duplicates(string):
  # Create an empty set
  duplicates = set()

  # For each character in the string
  for char in string:
    # If the character is already in the set, it is a duplicate
    if char in duplicates:
      print(f"'{char}' is a duplicate")
    else:
      # Add the character to the set
      duplicates.add(char)

# Test the function
find_duplicates("hello")
find_duplicates("world")
find_duplicates("abcdeabcde")

# Find duplicates in a list

def find_duplicates(lst):
  # Create an empty set
  duplicates = set()

  # For each element in the list
  for el in lst:
    # If the element is already in the set, it is a duplicate
    if el in duplicates:
      print(f"'{el}' is a duplicate")
    else:
      # Add the element to the set
      duplicates.add(el)

# Test the function
find_duplicates([1, 2, 3, 4, 5])
find_duplicates([1, 2, 2, 3, 3, 3])
find_duplicates([1, 1, 2, 2, 3, 3, 3])
