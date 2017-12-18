# Implement int sqrt(int x).

# Compute and return the square root of x.

# If x is not a perfect square, return floor(sqrt(x))

# Example :

# Input : 11
# Output : 3


class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        left = 0
        right = A
        while left <= right:
            mid = (left + right)/2
            next = mid +1
            if mid*mid<= A:
                if next*next > A:
                    return mid
                left = mid+1
            else:
                right = mid-1