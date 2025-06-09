
# ❓ Problem Statement:
# Given a string of lowercase letters, return the first character that does not repeat. If all characters repeat, return '_'.


# 📥 Input:
# A single string s with length between 1 and 10^5.
# Only lowercase English letters.

# 📤 Output:
# A single character: the first non-repeating character, or '_' if none exists.



inputString = input()
charDict = {}
for i in inputString:
    charDict[i] = charDict.get(i, 0) + 1

uniqueFound = True
for key in charDict:
    if charDict.get(key, 1) == 1:
        print(key)
        break
    else:
        uniqueFound = False
print("_") if not(uniqueFound) else None






















