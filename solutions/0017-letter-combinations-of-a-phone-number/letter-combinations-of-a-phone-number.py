# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
#
#
# Example:
#
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#
# Note:
#
# Although the above answer is in lexicographical order, your answer could be in any order you want.
#


#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (42.10%)
# Likes:    2302
# Dislikes: 310
# Total Accepted:    409.6K
# Total Submissions: 972.9K
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent.
# 
# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
# 
# 
# 
# Example:
# 
# 
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# Note:
# 
# Although the above answer is in lexicographical order, your answer could be
# in any order you want.
# 
#
class Solution:
    def back_track(self, start, digits, dictionary, current, final):
        
        if len(current) is len(digits):
            final.append(current)
            return
       
        for index in range(start, len(digits)):
            number = digits[index]
            string = dictionary[number]
            
            for char in string:
                self.back_track(index + 1, digits, dictionary, current + char, final)




    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) is 0:
            return []
        
        dictionary = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        result = []
        self.back_track(0,digits,dictionary, '', result)
        return result


