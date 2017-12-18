# Given a binary tree and a sum, find all root-to-leaf paths where each path’s sum equals the given sum.

# For example:
# Given the below binary tree and sum = 22,

#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]



# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root : root node of tree
    # @param sum1 : integer
    # @return a list of list of integers
    def pathSum(self, root, sum1):
        if not root:
            return []
        if not root.left and not root.right and sum1 == root.val:
            return [[root.val]]
        tmp = self.pathSum(root.left, sum1-root.val) + self.pathSum(root.right, sum1-root.val)
        return [[root.val]+i for i in tmp]