# ❓ Description:
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Two strings are anagrams if they contain the same characters but in a different order.

# 🔧 Function Signature:
# def group_anagrams(strs: list[str]) -> list[list[str]]:

# 🧪 Example:
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

# ✅ Constraints:
# 1 <= len(strs) <= 10^4
# 0 <= len(strs[i]) <= 100
# strs[i] consists of lowercase English letters.


inputList = ["eat", "tea", "tan", "ate", "nat", "bat"]
outputList = []

# for i in range(len(inputList)): # O(n)
#     tempDict = {}
#     for k in inputList[i]:
#         tempDict[k] = tempDict.get(k, 0) + 1

#     for j in range(i, len(inputList)):
#         tempDictTwo = {}
#         for l in inputList[j]:
#             tempDictTwo[l] = tempDictTwo[l]
         
#         anagram = True
#         if len(tempDictTwo) == len(tempDict): 
#             for m in 


for i in range(len(inputList)):
    # print(i)
    tempDict = {}
    for j in inputList[i]:
        tempDict[j] = tempDict.get(j, 0) + 1
    dictLength = len(tempDict)
    tempDictTemp = tempDict.copy()
    tempList = []
    for k in range(i + 1, len(inputList) - 1):
        if(inputList[k] != "Null"):
            for l in inputList[k]:
                tempDictTemp[l] = tempDictTemp.get(l, 0) + 1
            # print(tempDictTemp)
            if len(tempDict) == len(tempDictTemp):
                tempList.append(inputList[k])
                inputList[k] = "Null"
            else:
                tempDictTemp = tempDict.copy()
    if not(inputList[i]) == "Null":
        tempList.append(inputList[i])
        outputList.append(tempList) 
        # print(outputList)
        # print(inputList)     
print(outputList)

