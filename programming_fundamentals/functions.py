"""

Write a function named add that takes in two parameters x and y, both expected to be numbers. 
Your function should add the two numbers and return the result.

"""


def add(x, y):
    return x + y


"""

Write a funcion find_all_odds(lst), 
which takes in a list of integers and returns a new list containing all of the odd numbers of the
original list, in the order in which they appear. You can assume that lst will only contain integers.

"""


def find_all_odds(lst):

    # Declaring the new list
    lst2 = []

    # Checking each value to see which one is odd and then append that to the list which will get the new list of odd numbers

    for i in lst:
        if i % 2 == 1:
            lst2.append(i)

    # Returning lst2

    return lst2


"""

    Write the function string_lengths(strings), 
    which takes in a list of strings and returns a new list containing the lengths of the
    strings, in their relevant order. You can assume that strings will only contain strings.

"""


def string_lengths(strings):

    # Declaring the new list

    lst2 = []

    # Going to the elements of the list and adding the len of each string appending it to the new list
    for i in strings:
        lst2.append(len(i))

    # Returning the new list
    return lst2


"""

  Write a function named compare_lists.
  That accepts two optional parameters, lst1 and lst2

  The function should return the number of unique common elements between the two lists. 
  If either of the lists isn't passed as a parameter, it should be treated as an empty list.

  You can assume that the input lists will only contain integers.

"""


def compare_lists(lst1=[], lst2=[]):

    # Converting each list to a set

    lst1_set = set(lst1)
    lst2_set = set(lst2)

    # Checking the intersection of the sets and adding that value to set_intersection

    set_intersection = lst1_set.intersection(lst2_set)

    # Returning the len of set_intersection which will be the number of unique common elements between the two lists.
    return len(set_intersection)


"""

    Write the function trim_list(lst, elements_to_trim)
    Which takes in a list and returns a new version of the input list where the last elements_to_trim elements have been removed. 
    You can assume that elements_to_trim will always be a positive integer that's
    smaller than the length of lst.

"""


def trim_list(lst, elements_to_trim):

    # Declaring empty list

    trimmed_list = []

    # Goint to the elements of the list - the elements to trim

    for idx in range(len(lst) - elements_to_trim):

        # Saving current element in the list
        element = lst[idx]

        # Adding to the trimmed list the current element
        trimmed_list.append(element)

    # Returning the trimmed list
    return trimmed_list


"""

    Write the function running_sums(numbers)
    Which takes in a list of integers and returns a new list of the same length as numbers
    Where the element at index i in the new
    list is equal to numbers[0] + numbers[1] + ... + numbers[i - 1] + numbers[i]

"""


def running_sums(numbers):

    # Declaring an empty list
    sums = []

    # Making current_sum variable 0 to start

    current_sum = 0
    # Go to every value in the numbers list

    for number in numbers:
        # Add to current sum the current number in the list adding it so it add every time

        current_sum += number

        # Add to the sums list what we get to fill the new list
        sums.append(current_sum)

    # Return the new list with the sums
    return sums
