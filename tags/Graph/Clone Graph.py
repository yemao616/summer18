    

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

UndirectedGraphNode.__hash__ = lambda self: id(self)

class Solution:
    def __init__(self):
        self.visited = {}
    
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node not in self.visited:
            new_node = UndirectedGraphNode(node.label)
            self.visited[node] = new_node
            new_node.neighbors = [self.cloneGraph(neighbor) for neighbor in node.neighbors]
        return self.visited[node]


    def cloneGraph_bfs(self, node):
        from collections import deque
        if not node:
            return node
        q = deque()
        h = {}
        q.append(node)
        cnode = UndirectedGraphNode(node.label)
        h[node] = cnode
        while(len(q) > 0):
            t = q.popleft()
            for i in t.neighbors:
                if i not in h:
                    h[i] = UndirectedGraphNode(i.label)
                    q.append(i)
                h[t].neighbors.append(h[i])
                    
        return cnode


    def cloneGraph_dfs(self, node):
        if not node:
            return node
        root = UndirectedGraphNode(node.label)
        stack = [node]
        visit = {}
        visit[node.label] = root
        while stack:
            top = stack.pop()

            for n in top.neighbors:
                if n.label not in visit:
                    stack.append(n)
                    visit[n.label] = UndirectedGraphNode(n.label)
                visit[top.label].neighbors.append(visit[n.label])

        return root