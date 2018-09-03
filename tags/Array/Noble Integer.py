# Given an integer array, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p
# If such an integer is found return 1 else return -1.


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        for i, each in enumerate(A):
            if each == len(A)-1-i and (i == len(A)-1 or A[i+1] != each):
                return 1
                
        return -1