
# 📄 Problem Statement:
# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.

# 💡 Example:
# Input: nums = [1,1,1,2,2,3], k = 2  
# Output: [1,2]


inputList = [1,1,1,2,2,3,3,3,3,3,4]
k = 2
numDict = {}
for i in inputList: # O(n)
    numDict[i] = numDict.get(i, 0) + 1 

sortedNumTupleList = sorted(numDict.items(), key=lambda i: i[1], reverse=True) # O(n log n)
print(sortedNumTupleList)
for i in range(k): # O(k)
    print(sortedNumTupleList[i][0])


















