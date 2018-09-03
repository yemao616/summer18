# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

#  A height balanced BST : a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. 
# Example :


# Given A : 1 -> 2 -> 3
# A height balanced BST  :

#       2
#     /   \
#    1     3



# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the root node in the tree
    def sortedListToBST(self, A):
        ref = []
        while A:
            ref.append(A.val)
            A = A.next
            
        def bst(ref, start, end):
            if end <= start:
                return None
            ind = (start + end)/2
            curr_root = TreeNode(ref[ind])
            curr_root.left = bst(ref, start, ind)
            curr_root.right = bst(ref, ind+1, end)
            return curr_root
            
        return bst(ref, 0, len(ref))