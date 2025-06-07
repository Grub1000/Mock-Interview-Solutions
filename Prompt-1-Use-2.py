# Given a string s, find the first character that does not repeat and return its index. If it doesn't exist, return -1.
# 
# ✅ Constraints:
# 1 <= len(s) <= 10^5
# s contains only lowercase English letters.
# 
# 🧪 Examples:
# 
# Input:  s = "leetcode"
# Output: 0
# 
# Input:  s = "loveleetcode"
# Output: 2
# 
# Input:  s = "aabb"
# Output: -1


stringInput = input()
stringDict = {}
for i in stringInput:
    stringDict[i] = stringDict.get(i, 0) + 1
# print(stringDict)
count = 0
uniqueNotFound = True
for key in stringDict:
    count += 1
    if stringDict.get(key, 1) == 1:
        print(count - 1 )
        uniqueNotFound = False
        break
if uniqueNotFound:
    print(-1)

# Second attempt without dictionaries:

foundUnique = False
for i in range(len(stringInput)):
    matchFound = False
    for j in range( i + 1, len(stringInput)):
        if stringInput[i] != "0" and stringInput[i] == stringInput[j]:
            matchFound = True
            stringInput = stringInput.replace(stringInput[i], "0")
            # print(stringInput[i])
    if stringInput[i] != "0" and matchFound == False:
        print(i)
        foundUnique = True
        break
if not(foundUnique):
    print(-1)







    







