#
# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom 
# note can be constructed from the magazines ; otherwise, it will return false. 
#
#
# Each letter in the magazine string can only be used once in your ransom note.
#
#
# Note:
# You may assume that both strings contain only lowercase letters.
#
#
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
#
#


#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note/description/
#
# algorithms
# Easy (50.35%)
# Likes:    339
# Dislikes: 131
# Total Accepted:    118.6K
# Total Submissions: 235.5K
# Testcase Example:  '"a"\n"b"'
#
#
# Given an arbitrary ransom note string and another string containing letters
# from all the magazines, write a function that will return true if the ransom
# note can be constructed from the magazines ; otherwise, it will return
# false.
#
#
# Each letter in the magazine string can only be used once in your ransom
# note.
#
#
# Note:
# You may assume that both strings contain only lowercase letters.
#
#
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
#
#
#


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        dictionary = {}

        for c in magazine:
            if c not in dictionary:
                dictionary[c] = 1
            else:
                dictionary[c] = dictionary[c] + 1

        for c in ransomNote:
            if c not in dictionary:
                return False
            else:
                if dictionary[c] == 0:
                    return False
                else:
                    dictionary[c] = dictionary[c] - 1

        return True

