"""

    Write a function named replace that takes in three parameters: lst, target and swap_value
    Your function should replace all instances , and it shoudn't return
    anything; in other words, your function should mutate the input list.

"""

def replace(lst, target, swap_value):
    # Loop to the index of lst
    for idx in range(len(lst)):
        # Saying the current element is the current of the list
        element = lst[idx]

        # Checking if element is equal to target and if it is we modify the list with the value
        if element == target:
            lst[idx] = swap_value