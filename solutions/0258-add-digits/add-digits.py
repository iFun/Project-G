# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
#
# Example:
#
#
# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
#              Since 2 has only one digit, return it.
#
#
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?


#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#
# https://leetcode.com/problems/add-digits/description/
#
# algorithms
# Easy (54.64%)
# Likes:    503
# Dislikes: 835
# Total Accepted:    249.2K
# Total Submissions: 456.1K
# Testcase Example:  '38'
#
# Given a non-negative integer num, repeatedly add all its digits until the
# result has only one digit.
#
# Example:
#
#
# Input: 38
# Output: 2
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
# Since 2 has only one digit, return it.
#
#
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
#


class Solution:
    def addDigits(self, num: int) -> int:
        return num if num == 0 else num % 9 or 9

