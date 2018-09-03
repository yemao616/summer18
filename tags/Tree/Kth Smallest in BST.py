# Given a binary search tree, write a function to find the kth smallest element in the tree.

# Example :

# Input : 
#   2
#  / \
# 1   3

# and k = 2

# Return : 2

# As 2 is the second smallest element in the tree.
#  NOTE : You may assume 1 <= k <= Total number of nodes in BST 


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        self.l = []
        def inorder(A):
            if A is not None:
                inorder(A.left)
                self.l.append(A.val)
                inorder(A.right)
        inorder(A)
        return self.l[B-1]