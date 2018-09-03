# Given a binary tree, find the length of the longest consecutive sequence path.

# The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

# For example,
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
# Longest consecutive sequence path is 3-4-5, so return 3.
#    2
#     \
#      3
#     / 
#    2    
#   / 
#  1
# Longest consecutive sequence path is 2-3,not3-2-1, so return 2.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        max_count = [1]
        def DFS(node,count, parent_val):
            if parent_val +1 == node.val:
                count += 1
                max_count[0] = max(max_count[0], count)
            else:
                count = 1

            if node.left:
                DFS(node.left, count, node.val) 
            if node.right:
                DFS(node.right, count, node.val)
        DFS(root,1, root.val -2)

        return max_count[0]



    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, parent):
            if not node:
                return 0
            left = dfs(node.left, node)
            right = dfs(node.right, node)
            l[0] = max(l[0], left+1, right+1)
            if node.val == parent.val + 1:
                return max(left, right) + 1
            return 0
        l = [0]
        dfs(root, root)
        return l[0]