# 📝 Problem Statement
# You are given a string that may contain letters, numbers, spaces, and special characters. Write a function that cleans up the string by:
# 
# Removing all non-alphabetic characters (only keep letters a–z and A–Z).
# Converting all letters to lowercase.
# Returning the cleaned string.

# 📥 Input
# A single string, e.g., "Hello, World! 123".

# 📤 Output
# A cleaned string, e.g., "helloworld".

inputString = input()

def clean(i):
    if ord(i) > 64 and ord(i) < 91:
        return i.lower()
    elif ord(i) > 96 and ord(i) < 123:
        return i
    else:
        return ""
# charList = list(map(lambda i: clean(i), inputString.split() ))
charList = [clean(char) for char in inputString]
print(''.join(charList))

