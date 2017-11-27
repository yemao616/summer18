"""
    Refer: http://bookshadow.com/weblog/2017/03/19/leetcode-convert-bst-to-greater-tree/
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    total = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inOrder(node):
            if not node: return
            inOrder(node.right)
            node.val += self.total
            self.total = node.val
            inOrder(node.left)
        inOrder(root)
        return root
