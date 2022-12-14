# Code to remove duplicates from a string 

def duplicate_letters(text):
    # Create a new list using split function on text
	word_list = text.split()
    # Looping the word_list
	for word in word_list:
        # if the len of word is greater than the len of the set of word we return false
		if len(word) > len(set(word)):
			return False
	return True

# Removing duplicate characters from a string if order does not matter

string_to_check = input("Please enter a string: ")

# set() will create a set of unique letters in the string, and "".join() will join the letters back to a string in arbitrary order.
converted_str = "".join(set(string_to_check))

print(converted_str)

# Removing duplicate characters from a string if order does matter

# We use dict instead of a set since we care about the order and since Python 3.7 preserves the insertion order of the keys. 
result = "".join(dict.fromkeys(string_to_check))
print(result)