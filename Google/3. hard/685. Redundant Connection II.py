# In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

# The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

# The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v, where u is a parent of child v.

# Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

# Example 1:
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given directed graph will be like this:
#   1
#  / \
# v   v
# 2-->3
# Example 2:
# Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
# Output: [4,1]
# Explanation: The given directed graph will be like this:
# 5 <- 1 -> 2
#      ^    |
#      |    v
#      4 <- 3
# Note:
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.










"""
In this problem, you need to deal with 3 cases:

There is a loop in the graph, and no vertex has more than 1 parent.
Example:
Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
0_1506493498612_drawing2.jpg
In this case, you can simply output the edge in the loop that occurs last.
Union-find can be used to check whether an directed graph contains a cycle or not. At first, every vertex is an independent subset. For each edge, join the subsets that are on both sides of the edge. If both the vertices are in the same subset, a cycle is found.

A vertex has more than 1 parent, but there isn’t a loop in the graph.
Example:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
0_1506493289378_drawing 1.jpg
This case is also easy. You can just return the last edge that changes the tree into a graph. You can use an array of booleans to indicate whether a vertex has already got a parent.

A vertex has more than 1 parent, and is part of a loop.
Example:
Input: [[2,1], [3,1], [4,2], [1,4]]
Output: [2,1]
0_1506494193813_drawing3.jpg
Case 3 is a mixture of case 1 and case 2. If you detect both cases, do the following:
a. Find the vertex that has multiple parents. It is obvious that this vertex is also in the loop. In the example above, node 1 is what we are looking for.
b. Starting from this vertex, use DFS to find the last edge that forms the cycle.
c. Return this edge. In the example above, it is (2, 1).
"""

class Solution(object):         #O(N)
    def union(self, a, b):
        self.uf[self.find(b)] = self.find(a)

    def find(self, a):
        while self.uf[a] != a:
            a = self.uf[a]
        return a
    
    def detectCycle(self, V):
        self.visited[V] = True
        for i in range(len(self.adjList[V])):
            nextV = self.adjList[V][i]
            if self.visited[nextV]:
                return (V, nextV)
            ret = self.detectCycle(nextV)
            if ret[0]:
                return ret
        return (None, None)
    
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.uf = [0] + [i + 1 for i in range(len(edges))]
        self.adjList = [[] for i in range(len(edges) + 1)]      # Adjancency List
        hasFather = [False] * (len(edges) + 1)                  # Whether a vertex has already got a parent
        criticalEdge = None

        for i, edge in enumerate(edges):
            w, v = edge[0], edge[1]
            self.adjList[w].append(v)
            if hasFather[v]:
                criticalEdge = (w, v)                           # If a vertex has more than one parent, record the last edge
            hasFather[v] = True
            if self.find(w) == self.find(v):                    # If a loop is found, record the edge that occurs last
                cycleEdge = (w, v)
            self.union(w, v)

        if not criticalEdge:                                    # Case 1
            return cycleEdge
        self.visited = [False] * (len(edges) + 1)
        (w, v) = self.detectCycle(criticalEdge[1])
        return (w, v) if w else criticalEdge     