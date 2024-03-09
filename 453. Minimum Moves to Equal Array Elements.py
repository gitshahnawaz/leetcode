"""
453. Minimum Moves to Equal Array Elements
Solved
Medium
Topics
Companies
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment n - 1 elements of the array by 1.

 

Example 1:

Input: nums = [1,2,3]
Output: 3
Explanation: Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
Example 2:

Input: nums = [1,1,1]
Output: 0
"""



class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_num = min(nums)
        moves = sum(num - min_num for num in nums)
        
        return moves