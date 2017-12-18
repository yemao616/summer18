# Given a BST node, return the node which has value just greater than the given node.

# Example:

# Given the tree

#                100
#               /   \
#             98    102
#            /  \
#          96    99
#           \
#            97
# Given 97, you should return the node corresponding to 98 as thats the value just greater than 97 in the tree.
# If there are no successor in the tree ( the value is the largest in the tree, return NULL).

# Using recursion is not allowed.

# Assume that the value is always present in the tree.


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def getSuccessor(self, A, B):
        root = A
        succ = root
        while root.val != B:
            if B < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        if root.right != None:
            root = root.right
            while root.left!=None:
                    root = root.left
            return root
        else:
            if succ.val <= B:
                return None
            else:
                return succ
            
