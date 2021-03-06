# Implement a trie with insert, search, and startsWith methods.
#
# Example:
#
#
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
#
#
# Note:
#
#
# 	You may assume that all inputs are consist of lowercase letters a-z.
# 	All inputs are guaranteed to be non-empty strings.
#
#


#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (39.15%)
# Likes:    1657
# Dislikes: 34
# Total Accepted:    186K
# Total Submissions: 474.9K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# Implement a trie with insert, search, and startsWith methods.
# 
# Example:
# 
# 
# Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# 
# 
# Note:
# 
# 
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.
# 
# 
#
class Node:
    def __init__(self):
        self.map = {}
        self.endOfWord = False



class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if word is None:
            return None

        current = self.root

        for char in word:
            if char not in current.map:
                current.map[char] = Node()
            current = current.map[char]
        current.endOfWord = True
                
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word is None:
            return False
        current = self.root
        for char in word:
            if char not in current.map:
                return False
            else:
                current = current.map[char]
        
        return current.endOfWord

        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if prefix is None:
            return False
        current = self.root
        for char in prefix:
            if char not in current.map:
                return False
            else:
                current = current.map[char]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


