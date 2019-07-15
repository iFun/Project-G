#
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
#
#
#
#
# Note: You may assume the string contain only lowercase letters.
#


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) is 1:
            return 0
        
        dictionary = {}
        for char in s:
            if char in dictionary:
                dictionary[char] += 1
            else:
                dictionary[char] = 1
        index = 0      
        for char in s:
            if dictionary[char] is 1:
                return index
            else:
                index += 1
                
        return -1
