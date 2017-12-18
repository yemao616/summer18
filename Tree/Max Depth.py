# Given a binary tree, find its maximum depth.

# The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.

#  NOTE : The path has to end on a leaf node. 
# Example :

#          1
#         /
#        2
# max depth = 2.
def maxDepth(self, A):
        root = A
        if not root:
            return 0
        queue, depth = [root], 0
        while True:
            count = len(queue)
            if count == 0:
                return depth
            depth += 1
            while count:
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                count -= 1
        return depth
