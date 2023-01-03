# Code to reverse a list

# Slice will give us the elements back, we select -1 in the step in order to do that
# Start(Inclusive):Stop(Exclusive):Step

# Creating a list
my_list = [2,4,5,6,7,8,6]

# Reversing that list saving it into a new variable list called rev_list
rev_list = my_list[::-1]

# Using an f print to show the original list
print(f"Original list {my_list}")

# Printing the new reversed list
print(rev_list)