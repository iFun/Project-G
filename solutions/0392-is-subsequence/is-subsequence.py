#
# Given a string s and a string t, check if s is subsequence of t.
#
#
#
# You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
#
#
#
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).
#
#
# Example 1:
# s = "abc", t = "ahbgdc"
#
#
# Return true.
#
#
# Example 2:
# s = "axc", t = "ahbgdc"
#
#
# Return false.
#
#
# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?
#
# Credits:Special thanks to @pbrother for adding this problem and creating all test cases.


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) is len(t):
            return s is t
        if len(s) is 0:
            return True
        if len(t) is 0:
            return False
        
        x = 0
        y = 0
        
        while x < len(s) and y < len(t):
            if s[x] == t[y]:
                x += 1
            y += 1
        
        return x is len(s)
        
