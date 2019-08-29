# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
#
# Example 1:
#
#
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
#
# Example 2:
#
#
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
#
# Example 3:
#
#
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
#
# Example 4:
#
#
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
#
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
#


#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (35.23%)
# Likes:    668
# Dislikes: 82
# Total Accepted:    145.6K
# Total Submissions: 413.2K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
#
# Example 1:
#
#
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
#
# Example 2:
#
#
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
#
# Example 3:
#
#
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
#
# Example 4:
#
#
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
#
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters that may be separated by a single space.
#
#


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if not pattern:
            return False
        if ' ' not in str and len(pattern) is 1:
            return True
        strings = str.split()
        if len(strings) is not len(pattern):
            return False

        hash_table = {}
        hash_table_value = {}

        for i in range(0, len(pattern)):
            if pattern[i] in hash_table:
                if hash_table[pattern[i]] != strings[i]:
                    return False
            elif strings[i] in hash_table_value:
                if hash_table_value[strings[i]] != pattern[i]:
                    return False
            else:
                hash_table[pattern[i]] = strings[i]
                hash_table_value[strings[i]] = pattern[i]

        return True

