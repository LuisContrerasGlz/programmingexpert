# Algorithm to check a Palindrome

def isPalindrome(str):
    startIndex = 0
    endIndex = len(str) - 1

    for i in str:
        if str[startIndex] != str[endIndex]:
            return False
        return True


print(isPalindrome("racercar"))
