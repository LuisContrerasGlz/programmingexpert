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


"""

5. Use nested for loops to iterate through the provided list,
   which contains other lists, and print the respective sums of the inner
   lists, each on a separate line.

"""

lst = [[2, 3, 4], [-2, -4, 0], [1, 2], [1, 1, 1, 5, 6], [0, 9, 8, 7]]

for inner_list in lst:
    sum_of_inner_list = 0

    for item in inner_list:
        sum_of_inner_list += item

    print(sum_of_inner_list)

"""

6. Use a single for loop to iterate through the provided list of
   numbers, and for each number, print the sum of the number and the one
   directly to its right. In other words, print

"""

lst = [-2, 0, 4, 5, 1, 2]

for i in range(len(lst)-1):
        sum_of_items = lst[i] + lst[i + 1]
        print(sum_of_items)