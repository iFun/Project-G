#
# Given a non-empty string s, you may delete at most one character.  Judge whether you can make it a palindrome.
#
#
# Example 1:
#
# Input: "aba"
# Output: True
#
#
#
# Example 2:
#
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
#
#
#
# Note:
#
# The string will only contain lowercase characters a-z.
# The maximum length of the string is 50000.
#
#


#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (34.87%)
# Likes:    888
# Dislikes: 62
# Total Accepted:    91.1K
# Total Submissions: 261.2K
# Testcase Example:  '"aba"'
#
#
# Given a non-empty string s, you may delete at most one character.  Judge
# whether you can make it a palindrome.
#
#
# Example 1:
#
# Input: "aba"
# Output: True
#
#
#
# Example 2:
#
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
#
#
#
# Note:
#
# The string will only contain lowercase characters a-z.
# The maximum length of the string is 50000.
#
#
#


class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) < 3:
            return True
        if s == s[::-1]:
            return True

        left = 0
        right = len(s) - 1

        while (left < right):
            if s[left] != s[right]:
                newSLeft = s[:left] + s[(left+1):]
                newSRight = s[:right] + s[(right+1):]

                if newSLeft == newSLeft[::-1] or newSRight == newSRight[::-1]:
                    return True
                return False

            left += 1
            right -= 1

        return True

