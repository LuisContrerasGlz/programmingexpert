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