# Find largest distance
# Given an arbitrary unweighted rooted tree which consists of N (2 <= N <= 40000) nodes. The goal of the problem is to find largest distance between two nodes in a tree. Distance between two nodes is a number of edges on a path between the nodes (there will be a unique path between any pair of nodes since it is a tree). The nodes will be numbered 0 through N - 1.

# The tree is given as an array P, there is an edge between nodes P[i] and i (0 <= i < N). Exactly one of the i’s will have P[i] equal to -1, it will be root node.

#  Example:
# If given P is [-1, 0, 0, 0, 3], then node 0 is the root and the whole tree looks like this: 
#           0
#        /  |  \
#       1   2   3
#                \
#                 4  
#  One of the longest path is 1 -> 0 -> 3 -> 4 and its length is 3, thus the answer is 3. Note that there are other paths with maximal distance. 




from collections import defaultdict

class Solution:                         # two bfs, 1st to find the endpoint, 2nd to find the path
    # @param A : list of integers
    # @return an integer
    def solve(self, a):
        edge = defaultdict(list)
        for child, parent in enumerate(a):
            if parent != -1:
                edge[parent].append(child)
                edge[child].append(parent)
                
        answers = [-1, -1]
        
        def bfs(start):
            stack = [(start, -1, 0)]
            push, pop = stack.append, stack.pop
            
            while stack:
                source, previous, distance = pop()
                
                if distance > answers[0]:
                    answers[0], answers[1] = distance, source
                    
                for destination in edge[source]:
                    if destination != previous:
                        push((destination, source, distance + 1))
                        
        start = 0
        bfs(start)
        
        start = answers[1]
        answers = [-1, -1]
        bfs(start)
        
        return answers[0]