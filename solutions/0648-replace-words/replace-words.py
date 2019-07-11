# In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.
#
# Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.
#
# You need to output the sentence after the replacement.
#
# Example 1:
#
#
# Input: dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
#
#
#  
#
# Note:
#
#
# 	The input will only have lower-case letters.
# 	1 <= dict words number <= 1000
# 	1 <= sentence words number <= 1000
# 	1 <= root length <= 100
# 	1 <= sentence words length <= 1000
#
#
#  
#


#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#
# https://leetcode.com/problems/replace-words/description/
#
# algorithms
# Medium (52.31%)
# Likes:    458
# Dislikes: 110
# Total Accepted:    35.8K
# Total Submissions: 68.4K
# Testcase Example:  '["cat", "bat", "rat"]\n"the cattle was rattled by the battery"'
#
# In English, we have a concept called root, which can be followed by some
# other words to form another longer word - let's call this word successor. For
# example, the root an, followed by other, which can form another word
# another.
# 
# Now, given a dictionary consisting of many roots and a sentence. You need to
# replace all the successor in the sentence with the root forming it. If a
# successor has many roots can form it, replace it with the root with the
# shortest length.
# 
# You need to output the sentence after the replacement.
# 
# Example 1:
# 
# 
# Input: dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
# 
# 
# 
# 
# Note:
# 
# 
# The input will only have lower-case letters.
# 1 <= dict words number <= 1000
# 1 <= sentence words number <= 1000
# 1 <= root length <= 100
# 1 <= sentence words length <= 1000
# 
# 
# 
# 
#

class Solution:
    def replaceWords(self, roots, sentence):
        def _trie(): return collections.defaultdict(_trie)
        trie = _trie()
        END = True
        for root in roots:
            cur = trie
            for letter in root:
                cur = cur[letter]
            cur[END] = root

        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur:
                    break
                cur = cur[letter]
                if END in cur:
                    return cur[END]
            return word

        return " ".join(map(replace, sentence.split()))



