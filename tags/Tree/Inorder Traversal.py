# Given a binary tree, return the inorder traversal of its nodes’ values.

# Example :
# Given binary tree

#    1
#     \
#      2
#     /
#    3
# return [1,3,2].

# Using recursion is not allowed.

# See Expected Output



# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        stack, res = [], []
        current = A
        while current:
            stack.append(current)
            current = current.left
            while not current and len(stack) > 0:
                current = stack.pop()
                res.append(current.val)
                current = current.right
        return res

    def inorderTraversal2(self, A):
        self.ls = []
        if A!=None :
            self.ls.extend(self.inorderTraversal(A.left))
            self.ls.append(A.val)
            self.ls.extend(self.inorderTraversal(A.right))
        return self.ls