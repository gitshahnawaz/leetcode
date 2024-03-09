"""
792. Number of Matching Subsequences
Solved
Medium
Topics
Companies
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
"""



class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def isSubsequence(word):
            idx = -1

            for letter in word:
                idx = s.find(letter, idx+1)
                if idx == -1:
                    return False
            return True
        
        count = 0
        
        for word in words:
            if isSubsequence(word):
                count += 1

        return count