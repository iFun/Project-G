# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
#
# Example: 
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
#
#


#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (48.27%)
# Likes:    547
# Dislikes: 56
# Total Accepted:    100.6K
# Total Submissions: 208.5K
# Testcase Example:  '"abccccdd"'
#
# Given a string which consists of lowercase or uppercase letters, find the
# length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome
# here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
#
# Example:
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
#
#
#


class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0
        if len(s) is 1:
            return 1

        hash_table = {}
        result = 0

        for char in s:
            if char not in hash_table:
                hash_table[char] = 1
            else:
                hash_table[char] = hash_table[char] + 1

            if hash_table[char] % 2 == 0:
                result += 1

        if result * 2 != len(s):
            return result * 2 + 1
        else:
            return result * 2

