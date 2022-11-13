"""

    Write a function named replace that takes in three parameters: lst, target and swap_value
    Your function should replace all instances , and it shoudn't return
    anything; in other words, your function should mutate the input list.

"""

def replace(lst, target, swap_value):
    for idx in range(len(lst)):
        element = lst[idx]

        if element == target:
            lst[idx] = swap_value