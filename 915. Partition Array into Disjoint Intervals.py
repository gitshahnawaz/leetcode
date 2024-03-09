"""
915. Partition Array into Disjoint Intervals
Solved
Medium
Topics
Companies
Given an integer array nums, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.

Test cases are generated such that partitioning exists.

 

Example 1:

Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
Example 2:

Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]
"""



class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)

        left_max = max_till = nums[0]

        split_index = 0

        for i in range(1, n):
            max_till = max(nums[i], max_till)
            if nums[i] < left_max:
                left_max = max_till
                split_index = i
                
        
        return split_index + 1