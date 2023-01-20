# Count the items from a list using a Dictionary, calculating the frequency of elements in an array

# O(n) time complexity
array = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4]
diccionario = {}

for i in range(len(array)):
    if array[i] in diccionario:
        diccionario[array[i]] += 1
    else:
        diccionario[array[i]] = 1

print(diccionario)
"""

Here we loop the array/list and check if the element is in the dictionary
If it is we update the count by 1
If it is not we add it to the dictionary


"""
