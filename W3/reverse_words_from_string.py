"""
Reverse the worlds in a string

1. Split the string into words(making it a list).
2. Reverse the list of words.
3. Join the reversed list of words back into a string.

"""

def reverse_words(input_string):
    # Split the input string into words
    words = input_string.split()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join the reversed list of words back into a string
    reversed_string = ' '.join(reversed_words)
    return reversed_string

# Example usage
original_string = "Hello, World! How are you?"
reversed_string = reverse_words(original_string)
print("Original string:", original_string)
print("Reversed words string:", reversed_string)


"""
With For loop

1. Split the string into words.
2. Use a for loop to iterate through the words from the end to the beginning.
3. Append each word to a new list.
4. Join the list of reversed words back into a string.

"""

def reverse_words(input_string):
    # Split the input string into words
    words = input_string.split()
    # Initialize an empty list to store the reversed words
    reversed_words = []
    # Loop through the words list in reverse order
    for i in range(len(words) - 1, -1, -1):
        reversed_words.append(words[i])
    # Join the reversed list of words back into a string
    reversed_string = ' '.join(reversed_words)
    return reversed_string

# Example usage
original_string = "Hello, World! How are you?"
reversed_string = reverse_words(original_string)
print("Original string:", original_string)
print("Reversed words string:", reversed_string)



