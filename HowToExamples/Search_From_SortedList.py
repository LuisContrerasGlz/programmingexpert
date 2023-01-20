# Search a specific element from a list/array if the array is ordered

# Linear searching with target

testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
tarjet = 15

# Linear sort O(n)

for i in range(len(testArray)):
    if testArray[i] == tarjet:
        print("Found it at " + str(i))
