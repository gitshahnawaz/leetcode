"""
784. Letter Case Permutation
Solved
Medium
Topics
Companies
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

 

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]
"""



class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        res = []

        def dfs(cur_s, i):
            if len(cur_s) == len(s):
                res.append(cur_s)
            else:
                if s[i].isalpha():
                    dfs(cur_s + s[i].swapcase(),i+1)
                dfs(cur_s + s[i],i+1)
            
        dfs("",0)
        
        return res