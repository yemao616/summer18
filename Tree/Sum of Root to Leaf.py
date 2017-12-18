# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

# An example is the root-to-leaf path 1->2->3 which represents the number 123.

# Find the total sum of all root-to-leaf numbers % 1003.

# Example :

#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.

# Return the sum = (12 + 13) % 1003 = 25 % 1003 = 25.


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def sumNumbers2(self, A):
        root = A
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        tmp = self.sumNumbers2(root.left) + self.sumNumbers2(root.right)
        return [str(root.val)+ i for i in tmp]
        
    def sumNumbers(self, A):
        ans = self.sumNumbers2(A)
        total = 0
        for x in ans:
            total += int(x)
        return total%1003
        


##### method 2, smart!

     def traverse(self,A,val):
        if A==None:
            return 0
        val=(val*10+A.val)
        
        if A.left==None and A.right==None:
            return val
        
        return self.traverse(A.left,val)+self.traverse(A.right,val)
        
    def sumNumbers(self, A):
        return self.traverse(A,0)%1003


        