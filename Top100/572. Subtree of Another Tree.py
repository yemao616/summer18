# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def isSame(x, y):
            if not x and not y:
                return True
            if not x or not y:
                return False
            return x.val == y.val and isSame(x.left, y.left) and isSame(x.right, y.right)
        
        def preOrder(x, y):
            return x!= None and (isSame(x, y) or preOrder(x.left, y) or preOrder(x.right, y))
        
        return preOrder(s, t)
        