"""
516. Longest Palindromic Subsequence
Solved
Medium
Topics
Companies
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
"""



class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def helper(l,r):
            if l>r:
                return 0
            if l==r:
                return 1
            
            if s[l]==s[r]:
                return (2+helper(l+1,r-1)) 

            return max(helper(l+1,r),helper(l,r-1))
        return helper(0,len(s)-1)