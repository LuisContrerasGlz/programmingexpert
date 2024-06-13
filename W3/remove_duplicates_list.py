# Remove Duplicates From a Python List

"""
With a Dictionary:
    1. Create a dictionary, using the List items as keys. 
    This will automatically remove any duplicates because dictionaries cannot have duplicate keys.
    2. Then, convert the dictionary back into a list
"""

mylist = ["a", "b", "a", "c", "c"]
dict_no_dup = dict.fromkeys(mylist)
mylist = list(dict_no_dup)
print(mylist)

# Function 

def remove_dup_lst(x):
  return list(dict.fromkeys(x))

mylist = remove_dup_lst(["a", "b", "a", "c", "c"])

print(mylist)

"""

Using a set:

    1. Convert the list to a set to remove duplicates
    2. Convert the set back to a list

"""

def remove_duplicates(input_list):
    # Convert the list to a set to remove duplicates
    unique_elements = set(input_list)
    # Convert the set back to a list
    return list(unique_elements)

original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(original_list)
print("Original list:", original_list)
print("List after removing duplicates:", unique_list)
