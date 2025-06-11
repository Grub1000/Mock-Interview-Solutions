# Problem Statement: Longest Subarray with Sum K
# Given an array of integers nums and an integer k, return the length of the longest subarray whose sum is equal to k.
# If no such subarray exists, return 0.

# 🧪 Example:
# Input:
# nums = [1, -1, 5, -2, 3]
# k = 3

# Output:
# 4

# Explanation:
# The subarray [1, -1, 5, -2] sums to 3 and has length 4.


# Input:
# nums = [-2, -1, 2, 1]
# k = 1

# Output:
# 2

# Explanation:
# The subarray [2, 1] sums to 3, but [-1, 2] sums to 1, which is valid and has length 2.



# ✅ Constraints:
# 1 <= len(nums) <= 10^5

# -10^4 <= nums[i] <= 10^4

# -10^9 <= k <= 10^9

numList = [1, -1, 5, -2, 3]
subList = []
k = 3

total = 0
totalAdditions = 0
for i in range(len(numList)):
    tempList = []
    for j in range(i, len(numList)): # O(n^2)
        total = total + numList[j]
        tempList.append(numList[j])
        if total == k:
            subList.append(tempList.copy())
            tempList.clear()
            totalAdditions += 1
    tempList.clear()
    total = 0      

print(max(subList, key=len)) if totalAdditions > 0 else None












