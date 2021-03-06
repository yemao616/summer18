# You are given the following :

# A positive number N
# Heights : A list of heights of N persons standing in a queue
# Infronts : A list of numbers corresponding to each person (P) that gives the number of persons who are taller than P and standing in front of P
# You need to return list of actual order of persons’s height

# Consider that heights will be unique

# Example

# Input : 
# Heights: 5 3 2 6 1 4
# InFronts: 0 1 2 0 3 2
# Output : 
# actual order is: 5 3 2 1 6 4 
# So, you can see that for the person with height 5, there is no one taller than him who is in front of him, and hence Infronts has 0 for him.

# For person with height 3, there is 1 person ( Height : 5 ) in front of him who is taller than him.

# You can do similar inference for other people in the list.


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def order(self, A, B):			# TLE!
        n = len(A)
        res = [-1]*n
        A, B = zip(*sorted(zip(A, B)))
        for i in xrange(n):
            empty = B[i]
            sum_empty = 0
            for j in xrange(n):
                if res[j] == -1:
                    if sum_empty < empty:
                        sum_empty += 1
                    else:
                        res[j] = A[i]
                        break
                    
        return res



    def order(self, heights, infronts):
        pairs = zip(infronts, heights)
        pairs.sort(key = lambda x: x[1])
        #print pairs
        ans = [-1] * len(pairs)
        empties = range(0,len(pairs))
        for pos, h in pairs:
            k = empties.pop(pos)
            ans[k] = h
        return ans



"""segment Tree"""

class Node:
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.space = end - start
        self.left = None
        self.right = None
        
def build_tree(node):
    if node.end - node.start <= 1:
        return
    split = (node.start + node.end) / 2
    node.left = Node(node.start,split)
    node.right = Node(split,node.end)
    build_tree(node.left)
    build_tree(node.right)
    
def find_pos(node, infront):
    node.space -= 1
    if node.left is None:
        return node.start
    if node.left.space > infront:
        return find_pos(node.left, infront)
    else:
        return find_pos(node.right, infront - node.left.space)
        
        
class Solution:
    def order(self,heights,infronts):
        ret = [0]*len(heights)
        root = Node(0,len(heights))
        build_tree(root)
        
        for (h,i) in sorted(zip(heights,infronts)):
            pos = find_pos(root,i)
            ret[pos] = h
            
        return ret
Close

        
