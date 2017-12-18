# Suppose a sorted array A is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# Find the minimum element.

# The array will not contain duplicates.

# NOTE 1: Also think about the case when there are duplicates. Does your current solution work? How does the time complexity change?*
# PROBLEM APPROACH:

# Note: If you know the number of times the array is rotated, then this problem becomes trivial. If the number of rotation is x, then minimum element is A[x].
# Lets look at how we can calculate the number of times the array is rotated.


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        low, high = 0, len(A)-1
        ind = -1
        while low < high:
            mid = (low+high)/2
            next = mid+1
            prev = mid-1
            if A[low] <= A[high]:
                ind = low
                break
            elif A[mid]<= A[prev] and A[mid]<= A[next]:
                ind = mid
                break
            elif A[mid] >= A[low]:
                low = mid+1
            elif A[mid] <= A[high]:
                high = mid-1
        return A[ind]
       

    def findMin2(self, A):
        left = 0
        right = len(A)-1
        while left < right:
            mid = (left+right)/2
            if A[left] < A[right] or A[mid] < A[left]:
                right = mid
            else:
                left = mid+1
        return A[left]