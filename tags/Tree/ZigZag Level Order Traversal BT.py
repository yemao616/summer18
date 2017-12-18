# Given a binary tree, return the zigzag level order traversal of its nodes’ values. (ie, from left to right, then right to left for the next level and alternate between).

# Example : 
# Given binary tree

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return

# [
#          [3],
#          [20, 9],
#          [15, 7]
# ]


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        root = A
        if not root: return []
        res, temp, stack, flag=[], [], [root], 1
        while stack:
            for i in xrange(len(stack)):
                node = stack.pop(0)
                temp += [node.val]
                if node.left: stack+=[node.left]
                if node.right: stack+=[node.right]
            res+=[temp[::flag]]
            temp=[]
            flag*=-1
        return res