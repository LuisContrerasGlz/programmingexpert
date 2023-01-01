# Using a for loop:

def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

# Example
original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print(reversed_list) 

# Using the reversed function:

def reverse_list(lst):
    return list(reversed(lst))

# Example 
original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print(reversed_list)  

# Using the slice operator:

def reverse_list(lst):
    return lst[::-1]

# Example 
original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print(reversed_list) 


# Using the reverse method:

def reverse_list(lst):
    lst.reverse()
    return lst

# Example 
original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print(reversed_list) 
