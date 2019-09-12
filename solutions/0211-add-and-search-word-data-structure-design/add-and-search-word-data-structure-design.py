# Design a data structure that supports the following two operations:
#
#
# void addWord(word)
# bool search(word)
#
#
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
#
# Example:
#
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
#
#
# Note:
# You may assume that all words are consist of lowercase letters a-z.
#


#
# @lc app=leetcode id=211 lang=python3
#
# [211] Add and Search Word - Data structure design
#
# https://leetcode.com/problems/add-and-search-word-data-structure-design/description/
#
# algorithms
# Medium (30.82%)
# Likes:    883
# Dislikes: 55
# Total Accepted:    119.2K
# Total Submissions: 386.8K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# Design a data structure that supports the following two operations:
#
#
# void addWord(word)
# bool search(word)
#
#
# search(word) can search a literal word or a regular expression string
# containing only letters a-z or .. A . means it can represent any one letter.
#
# Example:
#
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
#
#
# Note:
# You may assume that all words are consist of lowercase letters a-z.
#
#


class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for c in word:
            current = current.children[c]

        current.isWord = True

    def search(self, word: str) -> bool:
        current = self.root
        self.result = False
        self.dfs(word, current)
        return self.result

    def dfs(self, word: str, current) -> bool:
        if not word:
            if current.isWord:
                self.result = True
            return

        if word[0] == '.':
            for n in current.children.values():
                self.dfs(word[1:], n)  # remove dot from word
        else:
            current = current.children.get(word[0])
            if not current:
                return
            self.dfs(word[1:], current)

