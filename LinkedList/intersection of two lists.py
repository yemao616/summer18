# Write a program to find the node at which the intersection of two singly linked lists begins.

# For example, the following two linked lists:


# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3

# begin to intersect at node c1.

#  Notes:
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):   
        
        def length( l ):
            len_list = 0
            while l :
                len_list += 1
                l = l.next
            return len_list
        
        lena = length(A)
        lenb = length(B)
        if lena > lenb:
            A, B= B, A
            d = lena - lenb
            lena, lenb = lenb, lena
        else:
            d = lenb - lena
        
        for i in range(d):
            B = B.next
        
        while A and B:
            if A == B:
                return A
            else:
                A = A.next
                B = B.next
        
        return None



    def getIntersectionNode(self, A, B):
        p1, p2 = A, B
        while p1 != p2:
            p1 = B if not p1 else p1.next
            p2 = A if not p2 else p2.next
        return p1