"""

w, x, y, z evaluates condition to true

"""

w = True
x = True
y = False
z = True

# `condition_` variables.
condition_1 = w and x and not y or not z
condition_2 = not (w and not w)
condition_3 = not (w and y or y)
condition_4 = x and (y or z and w)

# All of these should print `True`.
print(condition_1)
print(condition_2)
print(condition_3)
print(condition_4)