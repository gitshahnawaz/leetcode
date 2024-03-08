"""
503. Next Greater Element II
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.
"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        search = nums.copy()
        search.extend(nums)
        search.append(0)
        n = len(nums)
        res = []
        for i in range(len(nums)):
            for j in range(i,len(search)):
                if search[j] > nums[i] and j < len(search)-1:
                    res.append(search[j])
                    break
                elif j == len(search)-1:
                    res.append(-1)
                    break
        return res
                