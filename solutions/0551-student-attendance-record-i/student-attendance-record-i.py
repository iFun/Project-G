# You are given a string representing an attendance record for a student. The record only contains the following three characters:
#
#
#
# 'A' : Absent. 
# 'L' : Late.
#  'P' : Present. 
#
#
#
#
# A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).    
#
# You need to return whether the student could be rewarded according to his attendance record.
#
# Example 1:
#
# Input: "PPALLP"
# Output: True
#
#
#
# Example 2:
#
# Input: "PPALLL"
# Output: False
#
#
#
#
#


#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#
# https://leetcode.com/problems/student-attendance-record-i/description/
#
# algorithms
# Easy (45.57%)
# Likes:    166
# Dislikes: 638
# Total Accepted:    57.5K
# Total Submissions: 126.1K
# Testcase Example:  '"PPALLP"'
#
# You are given a string representing an attendance record for a student. The
# record only contains the following three characters:
#
#
#
# 'A' : Absent.
# 'L' : Late.
# ⁠'P' : Present.
#
#
#
#
# A student could be rewarded if his attendance record doesn't contain more
# than one 'A' (absent) or more than two continuous 'L' (late).
#
# You need to return whether the student could be rewarded according to his
# attendance record.
#
# Example 1:
#
# Input: "PPALLP"
# Output: True
#
#
#
# Example 2:
#
# Input: "PPALLL"
# Output: False
#
#
#
#
#
#


class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') <= 1 and 'LLL' not in s

