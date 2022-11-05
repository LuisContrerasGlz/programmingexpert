"""

Write a function named add that takes in two parameters x and y, both expected to be numbers. 
Your function should add the two numbers and return the result.

"""

def add(x,y):
    return x + y

"""

Write a funcion find_all_odds(lst), 
which takes in a list of integers and returns a new list containing all of the odd numbers of the
original list, in the order in which they appear. You can assume that lst will only contain integers.

"""

def find_all_odds(lst):
    lst2 = [] 
    
    for i in lst:
        if i % 2 == 1:
            lst2.append(i)

    return lst2


"""

    Write the function string_lengths(strings), 
    which takes in a list of strings and returns a new list containing the lengths of the
    strings, in their relevant order. You can assume that strings will only contain strings.

"""

def string_lengths(strings):

    lst2 = [] 
    
    for i in strings:
        lst2.append(len(i))
      
    return lst2
