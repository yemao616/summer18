# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

# Define a pair (u,v) which consists of one element from the first array and one element from the second array.

# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

# Example 1:
# Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

# Return: [1,2],[1,4],[1,6]

# The first 3 pairs are returned from the sequence:
# [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# Example 2:
# Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

# Return: [1,1],[1,1]

# The first 2 pairs are returned from the sequence:
# [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
# Example 3:
# Given nums1 = [1,2], nums2 = [3],  k = 3 

# Return: [1,3],[2,3]

# All possible pairs are returned from the sequence:
# [1,3],[2,3]



def kSmallestPairs(self, nums1, nums2, k):
    return sorted(itertools.product(nums1, nums2), key=sum)[:k]



def kSmallestPairs(self, nums1, nums2, k):  # O(mn logK)
    return heapq.nsmallest(k, ([u, v] for u in nums1 for v in nums2), key=sum)




class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        from heapq import heappush,heappop
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        ret = []
        pq = []
        for t in range(len(nums2)):
            heappush(pq,(nums1[0]+nums2[t],0,t))
        while len(pq) > 0 and len(ret) < k:
            node = heappop(pq)
            i = node[1]
            j = node[2]
            ret.append([nums1[i],nums2[j]])
            if i == len(nums1)-1:
                continue
            heappush(pq,(nums1[i+1]+nums2[j],i+1,j))
        return ret