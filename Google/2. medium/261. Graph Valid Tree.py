# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

# For example:

# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

# Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.




def validTree(self, n, edges):
    parent = range(n)
    def find(x):
        return x if parent[x] == x else find(parent[x])
    for e in edges:
        x, y = map(find, e)
        if x == y:
            return False
        parent[x] = y
    return len(edges) == n - 1




def validTree(self, n, edges):
    if len(edges) != n - 1:
        return False
    neighbors = {i: [] for i in range(n)}
    for v, w in edges:
        neighbors[v] += w,
        neighbors[w] += v,
    def visit(v):
        map(visit, neighbors.pop(v, []))
    visit(0)
    return not neighbors

	"""For an iterative version, just replace the three “visit” lines with"""

    stack = [0]
    while stack:
        stack += neighbors.pop(stack.pop(), [])



def validTree(self, n, edges):
    if len(edges) != n - 1:
        return False
    neighbors = {i: [] for i in range(n)}
    for v, w in edges:
        neighbors[v] += w,
        neighbors[w] += v,

    queue = collections.deque([0])
    while queue:
        queue.extend(neighbors.pop(queue.popleft(), []))
    return not neighbors


	