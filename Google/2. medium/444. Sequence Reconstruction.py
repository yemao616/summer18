# Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

# Example 1:

# Input:
# org: [1,2,3], seqs: [[1,2],[1,3]]

# Output:
# false

# Explanation:
# [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
# Example 2:

# Input:
# org: [1,2,3], seqs: [[1,2]]

# Output:
# false

# Explanation:
# The reconstructed sequence can only be [1,2].
# Example 3:

# Input:
# org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]

# Output:
# true

# Explanation:
# The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
# Example 4:

# Input:
# org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]

# Output:
# true




from collections import defaultdict


class Solution(object):
    def sequenceReconstruction(self, org, seqs):        # topological sort, parent before children

        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        adjacent = defaultdict(list)
        incoming_nodes = defaultdict(int)
        nodes = set()
        for arr in seqs:
            nodes |= set(arr)
            for i in xrange(len(arr)):
                if i == 0:
                    incoming_nodes[arr[i]] += 0
                if i < len(arr) - 1:
                    adjacent[arr[i]].append(arr[i + 1])
                    incoming_nodes[arr[i + 1]] += 1
        cur = [k for k in incoming_nodes if incoming_nodes[k] == 0]
        res = []
        while len(cur) == 1:
            cur_node = cur.pop()
            res.append(cur_node)
            for node in adjacent[cur_node]:
                incoming_nodes[node] -= 1
                if incoming_nodes[node] == 0:
                    cur.append(node)
        if len(cur) > 1:
            return False
        return len(res) == len(nodes) and res == org