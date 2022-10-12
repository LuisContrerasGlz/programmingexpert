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


"""

3. Use a single for loop to iterate through the two provided
    strings, and print all of their matching characters (i.e., the characters
    that are at the same index and that are equal to each other), each on a
    separate line.

"""

string1 = "aabbcsdw"
string2 = "abbbcsdd"

for idx in range(len(string1)):
    character1 = string1[idx]
    character2 = string2[idx]

    if character1 == character2:
        print(character1)

"""

4. Use a single for loop to iterate through the provided list, 
   and print the elements that are both divisible by 2 and located at
   an odd index, each on a separate line.

"""

lst = [45, 24, 22, 1, 45, 2, 12, 13, 16, 10, 0, -7]

for i in range(len(lst)):
    if (lst[i] % 2 == 0) and (i % 2 == 1):
        print(lst[i]) 