# Given an integer, write a function to determine if it is a power of three.
#
# Example 1:
#
#
# Input: 27
# Output: true
#
#
# Example 2:
#
#
# Input: 0
# Output: false
#
# Example 3:
#
#
# Input: 9
# Output: true
#
# Example 4:
#
#
# Input: 45
# Output: false
#
# Follow up:
# Could you do it without using any loop / recursion?


#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#
# https://leetcode.com/problems/power-of-three/description/
#
# algorithms
# Easy (41.82%)
# Likes:    322
# Dislikes: 1149
# Total Accepted:    201.1K
# Total Submissions: 480.9K
# Testcase Example:  '27'
#
# Given an integer, write a function to determine if it is a power of three.
#
# Example 1:
#
#
# Input: 27
# Output: true
#
#
# Example 2:
#
#
# Input: 0
# Output: false
#
# Example 3:
#
#
# Input: 9
# Output: true
#
# Example 4:
#
#
# Input: 45
# Output: false
#
# Follow up:
# Could you do it without using any loop / recursion?
#


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 1162261467=3^19. 3^20 is bigger than int.
        return n > 0 and 1162261467 % n == 0

