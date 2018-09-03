# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

# If there are multiple solutions, return any subset is fine.

# Example 1:

# nums: [1,2,3]

# Result: [1,2] (of course, [1,3] will also be ok)
# Example 2:

# nums: [1,2,4,8]

# Result: [1,2,4,8]



class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        S = {-1: set()}
        for x in sorted(nums):
            tmp = S.copy()
            for d in tmp:
                if x % d == 0 and (x not in S or len(S[x]) < len(S[d])):
                    S[x] = S[d]
            S[x] = S[x] | {x}		# S[x] is the subset end with x
        return list(max(S.values(), key=len))