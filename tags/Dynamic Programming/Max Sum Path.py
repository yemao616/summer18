# Given a binary tree, find the maximum path sum.

# The path may start and end at any node in the tree.

# Example :

# Given the below binary tree,

#        1
#       / \
#      2   3
# Return 6.


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxPathSum(self, A):
        def maxend(node):
            if not node:
                return 0
            left = maxend(node.left)
            right = maxend(node.right)
            self.max = max(self.max, left + node.val + right)
            return max(node.val + max(left, right), 0)
    
        self.max = None
        maxend(A)
        return self.max