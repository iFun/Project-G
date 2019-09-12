# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
# Example 1:
#
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
#
#
#
# Note:
# In the string, each word is separated by single space and there will not be any extra space in the string.
#


class Solution:
    def reverseWords(self, s: str) -> str:
        if not s or s == ' ' or len(s) is 1:
            return s
        result = ''
        tmp = ''
        for c in s:
            if c == ' ':
                result += tmp[::-1] + ' '
                tmp = ''
            else:
                tmp += c
        
        return result + tmp[::-1]
