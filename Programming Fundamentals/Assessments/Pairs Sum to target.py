"""

    Write a function that accepts two lists (list1 and list2) of integers and a target integer named target.
    Your function should return all pairs of indices in the form [x,y] where list1[x] + list2[y] == target.
    In other words, return the pairs of indices where the sum of their values equals target.
    lis1 and lis2 will always have the same number of elements and you may return the pairs in any order.

"""

# Decñaromg pir funtion with the parameters of list1, list2 and target


def pairs_sum_to_target(list1, list2, target):
    pairs = []

# Looping both lists
    for i, value1 in enumerate(list1):
        for j, value2 in enumerate(list2):
            # Checking if the values equal target and then appending the pair to the pairs list to return it later
            if value1 + value2 == target:
                pairs.append([i, j])

    return pairs
