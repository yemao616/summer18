# Given a binary tree, flatten it to a linked list in-place.

# Example :
# Given


#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:

#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
# Note that the left child of all nodes should be NULL.


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def makeflat(root):
    if(root==None):
        return 
    node=root
    while(node):
        if(node.left):
            rightmost=node.left
            while(rightmost.right):
                rightmost=rightmost.right
            rightmost.right=node.right
        
            node.right=node.left
            node.left=None
        node=node.right
    return root
        

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        return makeflat(A)


    def flatten(self, A):
        stack = [A]
        res = []
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)
        curr = dummy = TreeNode(0)
        for x in res:
            curr.right = TreeNode(x)
            curr = curr.right
        return dummy.right