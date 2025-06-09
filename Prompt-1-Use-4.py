# Problem Statement
# Write a function that determines if a given string has all unique characters. Return True if all characters in the string are unique, otherwise return False.

inputString = input()
charDict = {}
for i in inputString:
    charDict[i] = charDict.get(i, 0) + 1
result = True
for key in charDict:
    if charDict.get(key, 1) > 1:
        result = False
        break
    else:
        result = True
print(result)


# 🔄 Follow-Up Questions
# Optimization: Can you do this without using additional data structures?

# Edge Case Handling: How would you handle unicode or case sensitivity?

# Complexity Analysis: What is the time and space complexity of your solution?

# Extension: Modify the function to return the first non-unique character instead of just True or False.

# Same solution implementing the follow-up questions
inputString = input()

charDict = {}

for i in inputString:
    charDict[i] = charDict.get(i.lower(), 0) + 1

result = True
for key in charDict:
    if charDict.get(key, 1) > 1:
        print(key)
        result = False
        break
    else:
        result = True
print(result)
