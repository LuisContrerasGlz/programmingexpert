"""

Write a function that accepts any number of positional arguments, all of which you may assume will be lists of integers. Your function should filter all of these lists such that they only contain even positive integers and combine all of the lists into one list of Integers. Your function should then modify the combined list such that it contains the squares of all of the elements and return that list.

Use a combination of the map, filter and lambda functions/keywords to modify the lists.

"""


def flatten_lists(func):
    def wrapper(*args):
        new_args = []
        for arg in args:
            if isinstance(arg, list):
                new_args.extend(arg)
            else:
                new_args.append(arg)

        result = func(*new_args)
        return result

    return wrapper


def convert_strings_to_ints(func):
    def wrapper(*args):
        new_args = []
        for arg in args:
            if isinstance(arg, str) and arg.isdigit():
                new_args.append(int(arg))
            else:
                new_args.append(arg)

        result = func(*new_args)
        return result

    return wrapper


def filter_integers(func):
    def wrapper(*args):
        new_args = []
        for arg in args:
            if isinstance(arg, int):
                new_args.append(arg)

        result = func(*new_args)
        return result

    return wrapper


@flatten_lists
@convert_strings_to_ints
@filter_integers
def integer_sum(*args):
    return sum(args)
