# Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

# Note: The length of path between two nodes is represented by the number of edges between them.

# Example 1:

# Input:

#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output:

# 2
# Example 2:

# Input:

#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output:

# 2





# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def depth(node):
            left = right = 0
            if node.left:
                l_tmp = depth(node.left)
                if node.left.val == node.val:
                    left = l_tmp + 1
            if node.right:
                r_tmp = depth(node.right)
                if node.right.val == node.val:
                    right = r_tmp + 1

            self.res = max(self.res, left + right)
            return max(left, right)
        if not root:
            return 0
        depth(root)
        return self.res
        


class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        longest = [0]
        def traverse(node):
            if not node:
                return 0
            left_len, right_len = traverse(node.left), traverse(node.right)
            left = (left_len + 1) if node.left and node.left.val == node.val else 0
            right = (right_len + 1) if node.right and node.right.val == node.val else 0
            longest[0] = max(longest[0], left + right)
            return max(left, right)
        traverse(root)
        return longest[0]