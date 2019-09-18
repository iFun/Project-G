# Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
#
# Note:
#
# The given integer is guaranteed to fit within the range of a 32-bit signed integer.
# You could assume no leading zero bit in the integer’s binary representation.
#
#
#
# Example 1:
#
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
#
#
#
# Example 2:
#
# Input: 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
#
#


#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#
# https://leetcode.com/problems/number-complement/description/
#
# algorithms
# Easy (62.71%)
# Likes:    586
# Dislikes: 76
# Total Accepted:    114.7K
# Total Submissions: 183K
# Testcase Example:  '5'
#
# Given a positive integer, output its complement number. The complement
# strategy is to flip the bits of its binary representation.
#
# Note:
#
# The given integer is guaranteed to fit within the range of a 32-bit signed
# integer.
# You could assume no leading zero bit in the integer’s binary
# representation.
#
#
#
# Example 1:
#
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits),
# and its complement is 010. So you need to output 2.
#
#
#
# Example 2:
#
# Input: 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and
# its complement is 0. So you need to output 0.
#
#
#


class Solution:
    def findComplement(self, num: int) -> int:

        string = str(bin(num)[2:])
        result = ''
        for bit in string:
            if bit == '0':
                result += '1'
            else:
                result += '0'

        return int(result, 2)

