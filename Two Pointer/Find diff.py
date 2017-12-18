# Given an array ‘A’ of sorted integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

#  Example: Input : 
#     A : [1 3 5] 
#     k : 4
#  Output : YES as 5 - 1 = 4 
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem

# Try doing this in less than linear space complexity.


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):   # O(n^2)
        for i in xrange(len(A)):
            j = len(A)-1
            while j >i:
                if A[j] - A[i]  == B:
                    return 1
                elif A[j] - A[i] > B:
                    j -= 1
                else:
                    break
        return 0


    def diffPossible(self, A, B):
        i = 0
        j = 1
        while j < len(A):
            if A[j] - A[i] == B and i != j:
                return 1
            elif A[j] - A[i] > B:
                i += 1
            else:
                j += 1
        return 0