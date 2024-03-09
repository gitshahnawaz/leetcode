"""
720. Longest Word in Dictionary
Solved
Medium
Topics
Companies
Hint
Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

Note that the word should be built from left to right with each additional character being added to the end of a previous word. 

 

Example 1:

Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:

Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
"""




class Solution:
    def longestWord(self, words: List[str]) -> str:
        res = ''
        wordSet = set(words)

        for word in sorted(words):
           if len(word) > len(res):
               if all(word[:k] in wordSet for k in range(1, len(word))):
                   res = word
        return res