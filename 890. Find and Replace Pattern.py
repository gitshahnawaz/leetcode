"""

890. Find and Replace Pattern
Solved
Medium
Topics
Companies
Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

 

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.
Example 2:

Input: words = ["a","b","c"], pattern = "a"
Output: ["a","b","c"]
"""



class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        

        res = []

        def eligibility(word):
            d = {}
            for i in range(len(word)):

                if pattern[i] in d:
                    if d[pattern[i]] == word[i]:
                        continue
                    else:
                        return False
                d[pattern[i]] = word[i]
            
            return True
        
        def eligibility_pattern(word):
            d = {}
            for i in range(len(word)):

                if word[i] in d:
                    if d[word[i]] == pattern[i]:
                        continue
                    else:
                        return False
                d[word[i]] = pattern[i]
            
            return True


        for w in words:
            if eligibility(w) and eligibility_pattern(w):
                res.append(w)
        return res
            
            