"""
912. Sort an Array
Solved
Medium
Topics
Companies
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.
"""


class Solution:
    def merge(left, right):
            i, j = 0,0
            res = []
            while i < len(left) and j < len(left):
                if left[i] < right[j]:
                    res.append(left[i])
                    i+=1
                else:
                    res.append(right[j])
                    j+=1
            
            res.extend(left[i:])
            res.extend(right[j:])
            
            return res
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums

        mid =len(nums)//2

        left_arr = nums[:mid]
        right_arr = nums[mid:]

        left_arr = self.sortArray(left_arr)
        right_arr = self.sortArray(right_arr)

        return merge(left_arr, right_arr)

        
        


        