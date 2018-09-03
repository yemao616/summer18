# Sort a linked list using insertion sort.

# We have explained Insertion Sort at Slide 7 of Arrays

# Insertion Sort Wiki has some details on Insertion Sort as well.

# Example :

# Input : 1 -> 3 -> 2

# Return 1 -> 2 -> 3



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        l = []
        while A:
            l.append(A.val)
            A = A.next
        for i in xrange(1, len(l)):
            pivot = l[i]
            hole = i
            while (hole>0 and l[hole-1] >pivot):
                l[hole] = l[hole-1]
                hole -= 1
            l[hole] = pivot
            
        cur = dummy = ListNode(0)
        while l:
            cur.next = ListNode(l.pop(0))
            cur = cur.next
        return dummy.next