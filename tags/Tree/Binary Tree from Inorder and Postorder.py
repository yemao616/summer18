# Given inorder and postorder traversal of a tree, construct the binary tree.

#  Note: You may assume that duplicates do not exist in the tree. 
# Example :

# Input : 
#         Inorder : [2, 1, 3]
#         Postorder : [2, 3, 1]

# Return : 
#             1
#            / \
#           2   3



# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, inorder, postorder):
        if inorder and postorder:
            x = inorder.index(postorder.pop())
            root = TreeNode(inorder[x])
            root.right = self.buildTree(inorder[x+1:], postorder)
            root.left = self.buildTree(inorder[:x], postorder)
            return root