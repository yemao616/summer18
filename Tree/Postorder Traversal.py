# Given a binary tree, return the postorder traversal of its nodes’ values.

# Example :

# Given binary tree

#    1
#     \
#      2
#     /
#    3
# return [3,2,1].

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
    def postorderTraversal(self, A):
        if A is None:
            return
        stack = []
        ans = []
        root = A
        while True:
            while root:
                # Push root's right child and then root to stack
                if root.right is not None:
                    stack.append(root.right)
                stack.append(root)
                # Set root as root's left child
                root = root.left
            # Pop an item from stack and set it as root
            root = stack.pop()
            # If the popped item has a right child and the
            # right child is not processed yet, then make sure
            # right child is processed before root
            if root.right is not None and len(stack) > 0 and stack[-1] == root.right:
                stack.pop()  # Remove right child from stack 
                stack.append(root)  # Push root back to stack
                root = root.right  # change root so that the 
                # righ childis processed next
    
            # Else print root's data and set root as None
            else:
                ans.append(root.val)
                root = None
            if len(stack) <= 0:
                break
                
        return ans




    def postorderTraversal2(self, A):
        stack = [A]
        res = []
        while stack != []:
            curr = stack.pop()
            res.append(curr.val)
            if curr.left != None:
                stack.append(curr.left)
            if curr.right != None:
                stack.append(curr.right)
        return res[::-1]
