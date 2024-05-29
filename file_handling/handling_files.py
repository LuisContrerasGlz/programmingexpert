"""

The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists



"""
import os

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

"""
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content

"""

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

# Open the file "demofile3.txt" and overwrite the content:

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())

"""

To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist

"""

f = open("myfile.txt", "x")

f = open("myfile.txt", "w")

# To delete a file, you must import the OS module, and run its os.remove() function:

os.remove("demofile.txt")

# To avoid getting an error, you might want to check if the file exists before you try to delete it:

if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

# To delete an entire folder, use the os.rmdir() method:
  
os.rmdir("myfolder")

# You can only remove empty folders.