# Given an array of strings, group anagrams together.
#
# Example:
#
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
#
# Note:
#
#
# 	All inputs will be in lowercase.
# 	The order of your output does not matter.
#
#


#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (47.64%)
# Likes:    1768
# Dislikes: 116
# Total Accepted:    355.8K
# Total Submissions: 746.9K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
# 
# Example:
# 
# 
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# Note:
# 
# 
# All inputs will be in lowercase.
# The order of your output does not matter.
# 
# 
#
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for string in strs:
            sortedString = ''.join(sorted(string))
            if dic.get(sortedString) is not None:
                dic[sortedString].append(string)
            else:
                dic[sortedString] = [string]

        
        # result = []
        # for value in dic.values():
        #     result.append(value)
        return list(dic.values())

