# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.

# Note:

#  Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
# The solution set must not contain duplicate triplets. For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:
# (-1, 0, 1)
# (-1, -1, 2) 

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        A.sort()
        res = []
        for i in xrange(len(A)-2):
            left = i+1
            right = len(A)-1
            while left < right:
                s = A[i]+A[left]+A[right]
                if s > 0:
                    right -= 1
                    continue
                elif s == 0:
                    try:
                        res.index([A[i], A[left], A[right]])
                    except:
                        res.append([A[i], A[left], A[right]])
                left += 1
        return res
              

    def threeSum(self, A):
        n = len(A)

        A.sort()
        result = set()

        for i, v1 in enumerate(A):
            j, k = i + 1, n - 1
            while j < k:
                if A[i] + A[j] + A[k] == 0:
                    result.add((A[i], A[j], A[k]))
                    j += 1
                    k -= 1
                elif A[i] + A[j] + A[k] < 0:
                    j += 1
                else:
                    k -= 1

        return list(result)