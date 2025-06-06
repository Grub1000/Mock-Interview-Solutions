# 📌 Mock Interview Problem: Word Frequency Counter
# Problem Statement:
# Write a program that takes a paragraph of text as input and returns the top 3 most frequent words along with their counts.

# Words should be case-insensitive.

# Ignore punctuation.

# If there are fewer than 3 unique words, return all of them.

# Example Input:
# "The quick brown fox jumps over the lazy dog. The dog was not amused."

#Expected Output:
# the: 3
# dog: 2
# quick: 1


# Constraints:
# Assume input will be a single paragraph (string).
# You may use built-in libraries for string manipulation.
# Must run efficiently for up to 10,000 words.


inputString = "The quick brown fox jumps over the lazy dog. The dog was not amused."
substringList = list(map(lambda i: i.replace(".", ""), inputString.split()))
valueList = [["Padding", 1]]
if(len(substringList) > 2):
    for i in substringList:
        matchFound = False
        for j in valueList:
            if i.lower() == j[0]:
                j[1] = j[1] + 1
                matchFound = True
        if matchFound == False:
            valueList.append([i.lower(), 1])
    sortedValueList = sorted(valueList,key=lambda i: i[1])
    print(sorted(valueList,key=lambda i: i[1]))
    print(sortedValueList[-1])
    print(sortedValueList[-2])
    print(sortedValueList[-3])
else:
    for i in substringList:
        print(i)
