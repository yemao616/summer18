"""
~Hint: using dfs to visit the connected friends!!

"""

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visited = set()
        def dfs(nodes):
            for node, isfriend in enumerate(M[nodes]):
                if isfriend and node not in visited:
                    visited.add(node)
                    dfs(node)
        ans = 0
        for i in range(len(M)):
            if i not in visited:
                dfs(i)
                ans += 1
        return ans