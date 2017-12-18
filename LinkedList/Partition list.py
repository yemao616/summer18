# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        newhead = ListNode(0)
        newhead.next = A
        prev = newhead
        curr = tail = A
        l = 1
        while tail.next:
            l += 1
            tail = tail.next
        for i in xrange(l):
            if curr.val >= B and curr.next:
                prev.next = curr.next
                tail.next = curr
                tail = tail.next
                curr = curr.next
                tail.next = None
            else:
                prev = curr
                curr = curr.next
        return newhead.next