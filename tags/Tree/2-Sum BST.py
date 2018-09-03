# Given a binary search tree T, where each node contains a positive integer, and an integer K, you have to find whether or not there exist two different nodes A and B such that A.value + B.value = K.

# Return 1 to denote that two such nodes exist. Return 0, otherwise.

# Notes

# Your solution should run in linear time and not take memory more than O(height of T).
# Assume all values in BST are distinct.
# Example :

# Input 1: 

# T :       10
#          / \
#         9   20

# K = 19

# Return: 1

# Input 2: 

# T:        10
#          / \
#         9   20

# K = 40

# Return: 0




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
    def t2Sum(self, A, B):
        self.l = []
        def inorder(A):
            if A is not None:
                inorder(A.left)
                self.l.append(A.val)
                inorder(A.right)
        inorder(A)
        d = {}
        for i, elem in enumerate(self.l):
            if B-elem in d:
                return 1
            if elem not in d:
                d[elem] = i
        return 0


    def t2Sum(self, root, K):
        def helper(root, K, acc):
            if root is None or K == 0:
                return 0
            if root.val >= K:
                return helper(root.left, K, acc)
            if root.val in acc:
                return 1
            else:
                acc[K - root.val] = 1
                return helper(root.left, K, acc) or helper(root.right, K, acc)
        return helper(root, K, {})