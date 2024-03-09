"""
763. Partition Labels
Solved
Medium
Topics
Companies
Hint
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]
 
"""



class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []

        start = 0
        end = 0
        i=0
        for c in s:
            end = max(end,s.rfind(c))
            i+=1
            if i==end-start+1:
                res.append(i)
                start = end + 1
                i=0
        return res