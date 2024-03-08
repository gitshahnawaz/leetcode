"""
1324. Print Words Vertically
Solved
Medium
Topics
Companies
Hint
Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.

 

Example 1:

Input: s = "HOW ARE YOU"
Output: ["HAY","ORO","WEU"]
Explanation: Each word is printed vertically. 
 "HAY"
 "ORO"
 "WEU"
Example 2:

Input: s = "TO BE OR NOT TO BE"
Output: ["TBONTB","OEROOE","   T"]
Explanation: Trailing spaces is not allowed. 
"TBONTB"
"OEROOE"
"   T"
"""

class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = list(map(str, s.split()))
        
        m = max([len(st) for st in s])
        n = len(s)
        
        res = ["" for _ in range(m)]
        
        for i in range(len(s)):
            for j in range(m):
                if len(s[i]) <= j:
                    res[j] += " "
                else:
                    res[j] += s[i][j]

        
        return [r.rstrip() for r in res]
        