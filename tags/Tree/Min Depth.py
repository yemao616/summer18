# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def minDepth(self, A):
        """
        :type root: TreeNode
        :rtype: int
        """
        root = A
        if root:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            if not left or not right:
                return left+right+1
            else:
                return min(left, right)+1
        return 0

    def minDepth2(self, A):
            q = []
            q.append(A)
            q.append("sentinel")
            count = 0
            while q != ["sentinel"]:
                u = q[0]
                q = q[1:]
                if u == "sentinel": 
                    count += 1
                    q.append("sentinel")
                    continue
                if u.left: q.append(u.left)
                if u.right: q.append(u.right)
                if u.left == None and u.right == None : return count + 1
                
            return count + 1