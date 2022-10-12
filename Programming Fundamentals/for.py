"""

1. Use a single for loop to print the numbers in the range of 1 to 10 inclusive in a new line

"""

for i in range(1,11):
    print(i)


"""

2. User multiple for loops to iterate through the provided list,
   string, and tuple, and print all of their elements, each on a separate line.

   First print all of the list items, then all of the string characters, then
   all of the tuple items.

"""

lst = ["tim", "is", "the", "best", "instructor"]
string = "..."
tupl = ("and", "he", "is", "great")

for item in lst:
    print(item)

for character in string:
    print(character)

for item in tupl:
    print(item)