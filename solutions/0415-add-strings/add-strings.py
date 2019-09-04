# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.
#
#


#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#
# https://leetcode.com/problems/add-strings/description/
#
# algorithms
# Easy (44.36%)
# Likes:    488
# Dislikes: 163
# Total Accepted:    110.8K
# Total Submissions: 249.5K
# Testcase Example:  '"0"\n"0"'
#
# Given two non-negative integers num1 and num2 represented as string, return
# the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
#
#
#


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1 is '0':
            return num2
        if num2 is '0':
            return num1
        result = ''
        len1 = len(num1) - 1
        len2 = len(num2) - 1
        addone = 0

        while(len1 > -1 and len2 > -1):
            tmp = addone + int(num1[len1]) + int(num2[len2])
            if tmp > 9:
                tmp = tmp - 10
                addone = 1
            else:
                addone = 0

            result = str(tmp) + result
            len1 -= 1
            len2 -= 1

        while(len1 > -1):
            tmp = addone + int(num1[len1])
            if tmp > 9:
                tmp = tmp - 10
                addone = 1
            else:
                addone = 0

            result = str(tmp) + result
            len1 -= 1

        while(len2 > -1):
            tmp = addone + int(num2[len2])
            if tmp > 9:
                tmp = tmp - 10
                addone = 1
            else:
                addone = 0

            result = str(tmp) + result
            len2 -= 1

        if addone is 1:
            return '1' + result
        return result

