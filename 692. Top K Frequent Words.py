"""
692. Top K Frequent Words
Solved
Medium
Topics
Companies
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

 

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
"""



class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        res = []

        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
        
        for word,freq in sorted(d.items(), key = lambda x:(-x[1],x[0])):
           if k == 0:
               return res
           res.append(word)
           k-=1
           
        return res