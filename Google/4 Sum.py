# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

#  Note:
# Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
# The solution set must not contain duplicate quadruplets.
# Example : 
# Given array S = {1 0 -1 0 -2 2}, and target = 0
# A solution set is:

#     (-2, -1, 1, 2)
#     (-2,  0, 0, 2)
#     (-1,  0, 0, 1)
# Also make sure that the solution set is lexicographically sorted.
# Solution[i] < Solution[j] iff Solution[i][0] < Solution[j][0] OR (Solution[i][0] == Solution[j][0] AND ... Solution[i][k] < Solution[j][k])


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        seen = dict()
        A.sort()
        result = set()
        
        for i in xrange(len(A)):
            for j in xrange(i+1, len(A)):
                curr_sum = A[i] + A[j]
                diff = B - curr_sum
                if diff in seen:
                    for prev_sum in seen[diff]:
                        if A[prev_sum[1]] <= A[i] and i > prev_sum[1]:
                            result.add((A[prev_sum[0]], A[prev_sum[1]], A[i], A[j]))
                
                if curr_sum in seen:
                    seen[curr_sum].append((i, j))
                else:
                    seen[curr_sum] = [(i, j)]
        
        return sorted([list(item) for item in result])



    def fourSum(self, A, B):
        nums, target = A, B
        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
                return
            if N == 2: # two pointers solve sorted 2-sum problem
                l,r = 0,len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N
                for i in range(len(nums)-N+1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
    
        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results