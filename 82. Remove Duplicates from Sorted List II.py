"""
82. Remove Duplicates from Sorted List II
Solved
Medium
Topics
Companies
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            if current.next.val == current.next.next.val:

                duplicate_value = current.next.val
                while current.next and current.next.val == duplicate_value:
                    current.next = current.next.next
            else:
                current = current.next
        
        return dummy.next