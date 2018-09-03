# Given an array of integers, find the length of longest subsequence which is first increasing then decreasing.

# **Example: **

# For the given array [1 11 2 10 4 5 2 1]

# Longest subsequence is [1 2 10 4 2 1]

# Return value 6


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
           
        m=0
        L=[1]*len(A)
        for i in range(1,len(A)):
            for j in range(i):
                if A[j]<A[i]:
                    L[i]=max(L[i],L[j]+1)
        R=[1]*len(A)
        for i in range(len(A)-2,-1,-1):
            for j in range(len(A)-1,i,-1):
                if A[j]<A[i]:
                    R[i]=max(R[i],R[j]+1)
        for i in range(len(A)):
            val=L[i]+R[i]-1
            if val>m:
                m=val
        return m