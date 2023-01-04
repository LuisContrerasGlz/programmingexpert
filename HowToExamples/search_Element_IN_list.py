# Search for an element in a list
numbers = [3, 7, 2, 8, 4]

if 3 in numbers:
    print("3 is in the list")
else:
    print("3 is not in the list")

# To get the index in the list we can use the following:

# Search for an element in a list and get its index
numbers = [3, 7, 2, 8, 4]

try:
    index = numbers.index(8)
    print(f"8 is at index {index} in the list")
except ValueError:
    print("8 is not in the list")
