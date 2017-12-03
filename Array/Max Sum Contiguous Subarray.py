#Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
#For example:
#
#Given the array [-2,1,-3,4,-1,2,1,-5,4],
#
#the contiguous subarray [4,-1,2,1] has the largest sum = 6.
#
#For this problem, return the maximum sum.

class Solution:
    # @param A : tuple of integers
    # @return an integer

    def maxSubArray(A):
        s = 0
        res = a = b = A[0]
        for i in xrange(len(A)):
            s += A[i]
            if s < a:
                a = s
                b = s
            if s > b:
                b = s
                res = max(b - a, res)
        if res == A[0]:
            return max(A)
        return res


    def maxSubArray2(A):
        s = res = 0
        for i in xrange(len(A)):
            s += A[i]
            if s < 0:
                s = 0
            if res < s:
                res = s
#                print i
#                print "value: " + str(A[i])
        if res == 0:
            return max(A)
        return res
