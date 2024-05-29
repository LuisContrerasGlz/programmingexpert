"""

The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists



"""

f = open("demofile.txt")

f = open("demofile.txt", "r")
print(f.read())

# By default the read() method returns the whole text, but you can also specify how many characters you want to return:

f = open("demofile.txt", "r")
print(f.read(5))

# You can return one line by using the readline() method:

f = open("demofile.txt", "r")
print(f.readline())

# By calling readline() two times, you can read the two first lines:

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

# By looping through the lines of the file, you can read the whole file, line by line:

f = open("demofile.txt", "r")
for x in f:
  print(x)

# It is a good practice to always close the file when you are done with it.
  
f = open("demofile.txt", "r")
print(f.readline())
f.close()

