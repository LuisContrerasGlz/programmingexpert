w = 2
x = 2
y = -3
z = -1

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_slice = lst[::z]
second_slice = first_slice[:y]
third_slice = second_slice[x:]
last_slice = third_slice[::w]

print(last_slice)
