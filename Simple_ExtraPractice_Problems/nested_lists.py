# Declaring a nested list
cells = [["A1", "A2", "A3"], ["B1","B2","B3"]]

# Using nested for loop to iterate the lists 
for x in cells:
    for y in x:
        print("Element: ", y)