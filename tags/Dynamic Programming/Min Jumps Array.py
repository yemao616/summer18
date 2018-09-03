# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# Example :
# Given array A = [2,3,1,1,4]

# The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

# If it is not possible to reach the end index, return -1.


class Solution:
    # @param A : list of integers
    # @return an integer
    def jump(self, A):   # can handle 0
        n = len(A)
        if n == 0 or n == 1:
            return 0
        
        max_cur = 0
        steps = 0
        i=0
        while i < n:
            max_cur = i + A[i]
            if A[i] == 0:
                return -1
            else:
                steps += 1
            
            if max_cur >= n-1:
                return steps
            
            tmp = 0
            for j in range(i+1, max_cur+1):
                if A[j]+j > tmp:
                    tmp = A[j]+j
                    i = j
        
        return steps

