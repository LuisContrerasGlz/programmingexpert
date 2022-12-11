"""
An isogram is a word that has no repeating letters, consecutive or nonconsecutive. 
Create a function that takes a string and returns either true or false depending on whether or not it's an "isogram".

Examples
IsIsogram("Algorism") ➞ true

IsIsogram("PasSword") ➞ false
// Not case sensitive.

IsIsogram("Consecutive") ➞ false

"""

"""

1. Definir mi funcion IsIsogram con un string de parametro
2. Recorrer el string y revisar si es que hay ese caracter ya
3. Si esta regresamos falso
4. Si no regresamos true

"""

# First Option

def IsIsogram(word):
 
    # Convert the word in lower case.
    clean_word = word.lower()
 
    # Make an empty list to append unique letters
    letter_list = []
 
    for letter in clean_word:

        if letter in letter_list:
            return False
        letter_list.append(letter)
 
    return True


        