"""

Implement a function that takes a string that consists of lowercase letters and digits
and returns a string that consists of all digits and lowercase English letters that are not present in the string.
The digits should come first, in ascending order, followed by characters, also in ascending order.

Function Description:
missingCharacters has the following parameter(s):
    string s: a string

Return:
    string: a string as described above

Constrains:

0 <= length of s <= 100
Each character s[i] is in the range[a-z] or [0-9]
The resulting string will be non-empty


"""

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'missingCharacters' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def missingCharacters(s):
    # Create a set of all lowercase letters and digits
    all_chars = set('abcdefghijklmnopqrstuvwxyz0123456789')
    
    # Create a set of the characters present in the input string
    present_chars = set(s)
    
    # Compute the set of missing characters
    missing_chars = all_chars - present_chars
    
    # Sort the missing characters
    sorted_chars = sorted(missing_chars)
    
    # Return the sorted characters as a string
    return ''.join(sorted_chars)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = missingCharacters(s)

    fptr.write(result + '\n')

    fptr.close()