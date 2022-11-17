lst = [1,2,3,4,5,3,6,3]

x = int(input("Enter a number: "))

counter = 0
for i in lst:
    if lst[i] == x:
        counter += 1
print(f"There are {counter} repetitions of x")
