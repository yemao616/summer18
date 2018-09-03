# Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
# For example:
# Given BST [1,null,2,2],
#    1
#     \
#      2
#     /
#    2
# return [2].

# Note: If a tree has more than one mode, you can return them in any order.

# Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        count = collections.Counter()

        def dfs(node):
            if node:
                count[node.val] += 1
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        max_ct = max(count.itervalues())
        return [k for k, v in count.iteritems() if v == max_ct]



     def findMode(self, root):		# O(1)space, Morris Inorder Traversal
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.prev, self.count, self.maximum, self.res = None, 0, 0, []
        if not root: return []
        def update_count(val):
            if val == self.prev:
                self.count += 1
            else: # val != prev
                if self.prev is not None:
                    if self.count == self.maximum:
                        self.res.append(self.prev)
                    elif self.count > self.maximum:
                        self.res = [self.prev]
                self.maximum = max(self.count, self.maximum)
                self.prev = val
                self.count = 1
        
        while root:
            if not root.left:
                update_count(root.val)
                root = root.right
            else:
                pred = root.left
                while pred.right and pred.right is not root:
                    pred = pred.right
                if not pred.right:
                    pred.right = root
                    root = root.left
                else:
                    pred.right = None
                    update_count(root.val)
                    root = root.right
        if self.count > self.maximum:
            return [self.prev]
        if self.count == self.maximum:
            return self.res + [self.prev]
        return self.res