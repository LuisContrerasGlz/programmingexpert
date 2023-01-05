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
