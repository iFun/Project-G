# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
#
# Input: s = "anagram", t = "nagaram"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "rat", t = "car"
# Output: false
#
#
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?
#


#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (52.65%)
# Likes:    751
# Dislikes: 112
# Total Accepted:    357K
# Total Submissions: 678K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t , write a function to determine if t is an anagram
# of s.
#
# Example 1:
#
#
# Input: s = "anagram", t = "nagaram"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "rat", t = "car"
# Output: false
#
#
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?
#
#


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map = {}

        for char in s:
            if char in hash_map:
                hash_map[char] = hash_map[char] + 1
            else:
                hash_map[char] = 1

        for char in t:
            if char in hash_map:
                hash_map[char] = hash_map[char] - 1
                if hash_map[char] < 0:
                    print(hash_map[char])
                    return False
                if hash_map[char] is 0:
                    hash_map.pop(char, None)
            else:
                return False

        return len(hash_map) is 0

