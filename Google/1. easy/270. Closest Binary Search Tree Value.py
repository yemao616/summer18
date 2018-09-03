# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

# Note:
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return
        result = root.val
        while root:
            if abs(result - target) > abs(root.val - target):
                result = root.val
            if target == root.val:
                return result
            elif target < root.val:
                root = root.left
            else:
                root = root.right
        return result