# Description:
# Given a string s, find the length of the longest substring without repeating characters.

# 🔸 Function Signature:
# def length_of_longest_substring(s: str) -> int:
#     pass

# 🔸 Example:
# Input:
# s = "abcabcbb"

# Output:
# 3
# Explanation:
# The answer is "abc", with the length of 3.

# 🔸 More Examples:
# Input: s = "bbbbb"
# Output: 1

# Input: s = "pwwkew"
# Output: 3  # "wke" is the answer, not "pwke"

# 🔸 Constraints:
# 0 <= len(s) <= 10^5
# s consists of English letters, digits, symbols, and spaces.


s = "abcabcbb"
subStringLengthList = []
tempDict = {}

for j in range(len(s)):
    for i in range(j, len(s)):
        tempDict[s[i]] = tempDict.get(s[i], 0) + 1
        if tempDict.get(s[i], 0) == 2:
            print(tempDict)
            subStringLengthList.append(len(tempDict))
            tempDict = {}
            break
print(max(subStringLengthList))