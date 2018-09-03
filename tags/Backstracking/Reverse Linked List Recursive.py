# Reverse a linked list using recursion.

# Example :
# Given 1->2->3->4->5->NULL,

# return 5->4->3->2->1->NULL.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        return self.reverse(None, A)
    
    def reverse(self, prev, curr):
        if curr is None:
            return prev
        else:
            node = curr.next
            curr.next = prev
            return self.reverse(curr, node)