"""
95. Unique Binary Search Trees II
Solved
Medium
Topics
Companies
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 

Example 1:


Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0 :
            return []

        def generate_trees_helper(start,end):
            trees = []
            if start > end:
                trees.append(None)
                return trees
            
            for root_val in range(start, end+1):
                left_trees = generate_trees_helper(start, root_val -1)
                right_trees = generate_trees_helper(root_val + 1, end)

                for left_tree in left_trees:
                    for right_tree in right_trees:
                        root = TreeNode(root_val)
                        root.left = left_tree
                        root.right = right_tree
                        trees.append(root)
            return trees
        return generate_trees_helper(1,n)
    