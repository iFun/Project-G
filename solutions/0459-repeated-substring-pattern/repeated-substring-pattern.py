# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
#
#  
#
# Example 1:
#
#
# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.
#
#
# Example 2:
#
#
# Input: "aba"
# Output: False
#
#
# Example 3:
#
#
# Input: "abcabcabcabc"
# Output: True
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
#
#


#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#
# https://leetcode.com/problems/repeated-substring-pattern/description/
#
# algorithms
# Easy (40.47%)
# Likes:    882
# Dislikes: 106
# Total Accepted:    87.7K
# Total Submissions: 216.8K
# Testcase Example:  '"abab"'
#
# Given a non-empty string check if it can be constructed by taking a substring
# of it and appending multiple copies of the substring together. You may assume
# the given string consists of lowercase English letters only and its length
# will not exceed 10000.
#
#
#
# Example 1:
#
#
# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.
#
#
# Example 2:
#
#
# Input: "aba"
# Output: False
#
#
# Example 3:
#
#
# Input: "abcabcabcabc"
# Output: True
# Explanation: It's the substring "abc" four times. (And the substring "abcabc"
# twice.)

# I liked this solution and would like to explain this in a simple way.

# ss = (s + s)[1:-1]
# return ss.find(s) != -1

# The maximum length of a "repeated" substring that you could get from a string would be half it's length
# For example, s = "abcdabcd", "abcd" of len = 4, is the repeated substring.
# You cannot have a substring > (len(s)/2), that can be repeated.

# So, when ss = s + s, we will have atleast 4 parts of "repeated substring" in ss.
# (s+s)[1:-1], With this we are removing 1st char and last char = > Out of 4 parts of repeated substring, 2 part will be gone(they will no longer have the same substring).
# ss.find(s) != -1, But still we have 2 parts out of which we can make s. And that's how ss should have s, if s has repeated substring.


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False

        s1 = s + s
        s2 = s1[1:-1]  # removed first and last element

        return s2.find(s) != -1

