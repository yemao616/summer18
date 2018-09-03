# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

# Example 1:
#      0          3
#      |          |
#      1 --- 2    4
# Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

# Example 2:
#      0           4
#      |           |
#      1 --- 2 --- 3
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

# Note:
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = [set() for _ in xrange(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)
            
        visited = [False]*n
        def dfs(i):
            visited[i] = True
            for each in adj[i]:
                if not visited[each]:
                    dfs(each)
        ans = 0
        for i in xrange(n):
            if not visited[i]:
                ans += 1
                dfs(i)
        return ans
                