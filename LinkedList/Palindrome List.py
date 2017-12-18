# Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.

# Notes:

# Expected solution is linear in time and constant in space.
# For example,

# List 1-->2-->1 is a palindrome.
# List 1-->2-->3 is not a palindrome.





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        s = []
        while A:
            s.append(A.val)
            A = A.next
        s2 = s[::-1]
        if s == s2:
            return 1
        return 0