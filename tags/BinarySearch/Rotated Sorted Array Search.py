# Suppose a sorted array is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).

# You are given a target value to search. If found in the array, return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Input : [4 5 6 7 0 1 2] and target = 4
# Output : 0



class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        left = 0
        right = len(A)-1
        while left < right:
            mid = (left+right)/2
            if A[left] < A[right] or A[mid] < A[left]:
                right = mid
            else:
                left = mid +1
                
        low, high = 0, len(A)-1
        while low <= high:
            ind = (low+high)/2
            indx = (ind+left)%len(A)
            if A[indx] == B:
                return indx
            elif A[indx] > B:
                high = ind-1
            else:
                low = ind + 1
        return -1