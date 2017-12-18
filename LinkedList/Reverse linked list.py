# Reverse a linked list. Do it in-place and in one-pass.

# For example:
# Given 1->2->3->4->5->NULL,

# return 5->4->3->2->1->NULL.

# PROBLEM APPROACH :






# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        stack = []
        while A:
            stack.append(A.val)
            A = A.next
        new = ListNode(0)
        head = new
        while stack:
            cur = ListNode(stack.pop())
            new.next = cur
            new = new.next
        return head.next

    def reverse_list(self, A):
        prev, curr, nextn = None, A, None
        while curr:
            nextn = curr.next
            curr.next = prev
            prev = curr
            curr = nextn
        return prev