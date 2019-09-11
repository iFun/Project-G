# We are given two strings, A and B.
#
# A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.
#
#
# Example 1:
# Input: A = 'abcde', B = 'cdeab'
# Output: true
#
# Example 2:
# Input: A = 'abcde', B = 'abced'
# Output: false
#
#
# Note:
#
#
# 	A and B will have length at most 100.
#
#


#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#
# https://leetcode.com/problems/rotate-string/description/
#
# algorithms
# Easy (49.23%)
# Likes:    445
# Dislikes: 39
# Total Accepted:    46.5K
# Total Submissions: 94.4K
# Testcase Example:  '"abcde"\n"cdeab"'
#
# We are given two strings, A and B.
#
# A shift on A consists of taking string A and moving the leftmost character to
# the rightmost position. For example, if A = 'abcde', then it will be 'bcdea'
# after one shift on A. Return True if and only if A can become B after some
# number of shifts on A.
#
#
# Example 1:
# Input: A = 'abcde', B = 'cdeab'
# Output: true
#
# Example 2:
# Input: A = 'abcde', B = 'abced'
# Output: false
#
#
# Note:
#
#
# A and B will have length at most 100.
#
#
#


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and A in B + B

