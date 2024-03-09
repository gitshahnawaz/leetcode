"""
916. Word Subsets
Solved
Medium
Topics
Companies
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

 

Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]
"""



class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        d, ans = defaultdict(int), []

        for word in words2:                     #  <-- 1)
            c2 = Counter(word)
            for ch in c2:
                d[ch] = max(d[ch], c2[ch])

        for word in words1:                     #  <-- 2)
            c1 = Counter(word)

            for ch in d:
                if c1[ch] < d[ch]: break
            else:
                ans.append(word)                #  <-- else executes only if the for-loop
                                                #      completes without break

        return ans  