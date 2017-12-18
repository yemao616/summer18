# Given a binary tree, return the preorder traversal of its nodes’ values.

# Example :
# Given binary tree

#    1
#     \
#      2
#     /
#    3
# return [1,2,3].

# Using recursion is not allowed.


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversal(self, A):
        stack = [A]
        res = []
        while stack != []:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right != None:
                stack.append(curr.right)
            if curr.left != None:
                stack.append(curr.left)
        return res

