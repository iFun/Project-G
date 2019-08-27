# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
#
# Input: 123
# Output: 321
#
#
# Example 2:
#
#
# Input: -123
# Output: -321
#
#
# Example 3:
#
#
# Input: 120
# Output: 21
#
#
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
#


class Solution:
    def reverse(self, x: int) -> int:
        if x < 10 and x > -10:
            return x
        
        y = abs(x)
        result = 0
        while y > 0:
            digit = y % 10
            
            result = result * 10 + digit
            y = int(y / 10)
        
        if result > 0x7FFFFFFF:
            return 0
        
        
        if x < 0:
            return -1 * result
        return result
