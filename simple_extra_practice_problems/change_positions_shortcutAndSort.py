# Changing the position using assigment shorcut

first = input("Enter first number: ")
second = input("Enter second number: ")
print("Before swapping: ", first, second)

first, second = second, first

print("After swapping: ", first, second)

# Applying it with list

top_cities = ["New York", "Los Angeles", "Chicago", "Phoenix"]
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities)

# Sorting the list

top_cities.sort()

# Sorting numeric list

random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort()

# Reversing with keyword to be reverse
random_numbers.sort(reverse=True)

# Now using the sorted function

print(sorted(top_cities))
