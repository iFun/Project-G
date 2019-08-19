# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# Example:
#
#
# Input: "Hello World"
# Output: 5
#
#
#  
#


#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (32.27%)
# Likes:    406
# Dislikes: 1692
# Total Accepted:    283.7K
# Total Submissions: 878.9K
# Testcase Example:  '"Hello World"'
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word in the string.
# 
# If the last word does not exist, return 0.
# 
# Note: A word is defined as a character sequence consists of non-space
# characters only.
# 
# Example:
# 
# 
# Input: "Hello World"
# Output: 5
# 
# 
# 
# 
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        if len(s) is 1:
            if s[0] is " ":
                return 0
            return 1

        count = 0
        for char in reversed(s):
            if char is " " and count is not 0:
                return count
            else:
                if char is not " ":
                    count += 1
                
        
        return count


