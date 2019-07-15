# Given a string, sort it in decreasing order based on the frequency of characters.
#
# Example 1:
#
# Input:
# "tree"
#
# Output:
# "eert"
#
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
#
#
#
# Example 2:
#
# Input:
# "cccaaa"
#
# Output:
# "cccaaa"
#
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
#
#
#
# Example 3:
#
# Input:
# "Aabb"
#
# Output:
# "bbAa"
#
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
#
#


class Solution:
    def frequencySort(self, s: str) -> str:
        if s is None or len(s) is 1:
            return s
        
        dictionary = {}
        maxLength = 0
        for char in s:
            if char in dictionary:
                dictionary[char] += 1
            else:
                dictionary[char] = 1
            maxLength = max(maxLength,dictionary[char])
        
        bucket = [None] * (maxLength + 1)
        for key, value in dictionary.items():
            if bucket[value] is None:
                bucket[value] = [key]
            else:
                bucket[value].append(key)
        result = ''
        
        for index in range(len(bucket) - 1,0,-1):
            if bucket[index] is not None:
                for char in bucket[index]:
                    result += char * index
        
        return result
