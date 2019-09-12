#
# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
#
#
# Example:
#
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
#
#
#
# Restrictions: 
#
#  The string consists of lower English letters only.
#  Length of the given string and k will in the range [1, 10000]
#


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if not s or len(s) is 1:
            return s
        
        if k >= len(s):
            return s[::-1]
        counter = 0
        tmp = ''
        result = ''
        
        
        for c in s:
            
            if counter == k:
                result += tmp[::-1]
                tmp = ''
                counter += 1
            elif counter == 2 * k:
                result += tmp
                tmp = ''
                counter = 1
            else:
                counter += 1
            
            tmp += c
        
        if counter > k and counter <= 2 * k:
            return result + tmp
        
        return result + tmp[::-1]
