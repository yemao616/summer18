# Remove Element

# Given an array and a value, remove all the instances of that value in the array. 
# Also return the number of elements left in the array after the operation.
# It does not matter what is left beyond the expected length.

#  Example:
# If array A is [4, 1, 1, 2, 1, 3]
# and value elem is 1, 
# then new length is 3, and A is now [4, 2, 3] 
# Try to do it in less than linear additional space complexity.


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        ind = 0
        for i in xrange(len(A)):
            if A[i] == B:
                continue
            A[ind] = A[i]
            ind += 1
        return ind
             

    def removeElement(self, A, B):
        A [:]= [i for i in A if i!=B]
        return len(A)