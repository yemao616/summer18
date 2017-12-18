# Given a sorted linked list, delete all duplicates such that each element appear only once.

# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        prev, curr = None, A
        while curr:
            if prev:
                if prev.val == curr.val:
                    prev.next = curr.next
                    curr = curr.next
                    continue
            prev = curr
            curr = curr.next
        return A



    def deleteDuplicates(self, A):
        head = A
        while A:
            while A.next and A.next.val == A.val:
                A.next = A.next.next
            A = A.next
        return head