#
# Implement a magic directory with buildDict, and search methods.
#
#
#
# For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.
#
#
#
# For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.
#
#
# Example 1:
#
# Input: buildDict(["hello", "leetcode"]), Output: Null
# Input: search("hello"), Output: False
# Input: search("hhllo"), Output: True
# Input: search("hell"), Output: False
# Input: search("leetcoded"), Output: False
#
#
#
# Note:
#
# You may assume that all the inputs are consist of lowercase letters a-z.
# For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
# Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.
#
#


#
# @lc app=leetcode id=676 lang=python3
#
# [676] Implement Magic Dictionary
#
# https://leetcode.com/problems/implement-magic-dictionary/description/
#
# algorithms
# Medium (51.78%)
# Likes:    381
# Dislikes: 100
# Total Accepted:    26.6K
# Total Submissions: 51.4K
# Testcase Example:  '["MagicDictionary", "buildDict", "search", "search", "search", "search"]\n[[], [["hello","leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]'
#
# 
# Implement a magic directory with buildDict, and search methods.
# 
# 
# 
# For the method buildDict, you'll be given a list of non-repetitive words to
# build a dictionary.
# 
# 
# 
# For the method search, you'll be given a word, and judge whether if you
# modify exactly one character into another character in this word, the
# modified word is in the dictionary you just built.
# 
# 
# Example 1:
# 
# Input: buildDict(["hello", "leetcode"]), Output: Null
# Input: search("hello"), Output: False
# Input: search("hhllo"), Output: True
# Input: search("hell"), Output: False
# Input: search("leetcoded"), Output: False
# 
# 
# 
# Note:
# 
# You may assume that all the inputs are consist of lowercase letters a-z.
# For contest purpose, the test data is rather small by now. You could think
# about highly efficient algorithm after the contest.
# Please remember to RESET your class variables declared in class
# MagicDictionary, as static/class variables are persisted across multiple test
# cases. Please see here for more details.
# 
# 
#
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            length = len(word)
            if length in self.map:
                self.map[length].append(word)
            else:
                self.map[length] = [word]
        

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        length = len(word)
        if length not in self.map:
            return False
        
        words = self.map[length]
        mismatch = 0
        for string in words:
            for i in range(length):
                if word[i] is not string[i]:
                    mismatch += 1
                if mismatch > 1:
                    continue
            if mismatch is 1:
                return True
            mismatch = 0
        
        return False
    
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)


