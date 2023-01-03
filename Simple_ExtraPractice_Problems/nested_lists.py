# Declaring a nested list
table = [["A1", "A2", "A3"], ["B1","B2","B3"]]

# Using nested for loop to iterate the lists 
for row in table:
    for cell in row:
        print("Element: ", cell)

