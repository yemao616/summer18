# Given an array of positive elements, you have to flip the sign of some of its elements such that the resultant sum of the elements of array should be minimum non-negative(as close to zero as possible). Return the minimum no. of elements whose sign needs to be flipped such that the resultant sum is minimum non-negative.

# Constraints:

#  1 <= n <= 100
# Sum of all the elements will not exceed 10,000.

# Example:

# A = [15, 10, 6]
# ans = 1 (Here, we will flip the sign of 15 and the resultant sum will be 1 )

# A = [14, 10, 4]
# ans = 1 (Here, we will flip the sign of 14 and the resultant sum will be 0)

#  Note that flipping the sign of 10 and 4 also gives the resultant sum 0 but flippings there are not minimum 


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, A):
        INF = len(A)+1
        s = sum(A)
        ans = [INF]*(s+1)
        ans[0] = 0
        for a in A :
            for i in reversed(range(s//2+1-a)) :
                ans[i+a] = min(ans[i+a], ans[i]+1)
        i = s//2+1
        while ans[i] == INF :
            i -= 1
        return ans[i]
            