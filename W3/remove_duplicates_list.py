# Remove Duplicates From a Python List

"""
With a Dictionary:
    1. Create a dictionary, using the List items as keys. 
    This will automatically remove any duplicates because dictionaries cannot have duplicate keys.
    2. Then, convert the dictionary back into a list
"""

mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)