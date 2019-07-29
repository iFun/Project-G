# Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.
#
#  
#
# Example 1:
#
#
#
# Input: A = "ab", B = "ba"
# Output: true
#
#
#
# Example 2:
#
#
# Input: A = "ab", B = "ab"
# Output: false
#
#
#
# Example 3:
#
#
# Input: A = "aa", B = "aa"
# Output: true
#
#
#
# Example 4:
#
#
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
#
#
#
# Example 5:
#
#
# Input: A = "", B = "aa"
# Output: false
#
#
#  
#
# Note:
#
#
# 	0 <= A.length <= 20000
# 	0 <= B.length <= 20000
# 	A and B consist only of lowercase letters.
#
#
#
#
#
#
#


#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#
# https://leetcode.com/problems/buddy-strings/descrip
# tion/
#
# algorithms
# Easy (27.69%)
# Likes:    305
# Dislikes: 189
# Total Accepted:    26.3K
# Total Submissions: 94.9K
# Testcase Example:  '"ab"\n"ba"'
#
# Given two strings A and B of lowercase letters, return true if and only if we
# can swap two letters in A so that the result equals B.
# 
# 
# 
# Example 1:
# 
# 
# 
# Input: A = "ab", B = "ba"
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: A = "ab", B = "ab"
# Output: false
# 
# 
# 
# Example 3:
# 
# 
# Input: A = "aa", B = "aa"
# Output: true
# 
# 
# 
# Example 4:
# 
# 
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
# 
# 
# 
# Example 5:
# 
# 
# Input: A = "", B = "aa"
# Output: false
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A and B consist only of lowercase letters.
# 
# 
# 
# 
# 
# 
# 
#
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) or set(A) != set(B):
            return False
        if A == B:
            return len(A) - len(set(A)) >= 1
        swapA = ''
        swapB = ''
        swaped = False
        for index in range(len(A)):
            if A[index] != B[index]:
                if swaped:
                    return False

                if len(swapA) > 0:
                    if B[index] == swapB and A[index] == swapA:
                        swaped = True
                    else:
                        return False
                else:
                    swapA = B[index]
                    swapB = A[index]
        if len(A) > 2:
            return True
        return swaped
                
                


