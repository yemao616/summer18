# Given a binary tree, print a vertical order traversal of it.

# Example :
# Given binary tree:

#       6
#     /   \
#    3     7
#   / \     \
#  2   5     9
# returns

# [
#     [2],
#     [3],
#     [6 5],
#     [7],
#     [9]
# ]


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def verticalOrderTraversal(self, A):
        cols = collections.defaultdict(list)
        queue = [(A, 0)]
        for node, i in queue:
            if node:
                cols[i].append(node.val)
                queue += (node.left, i - 1), (node.right, i + 1)
        return [cols[i] for i in sorted(cols)]
            
            