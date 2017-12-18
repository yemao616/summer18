# Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than O(n) space and traversing the stream sequentially O(1) times.

# Sample Input:

# [3 4 1 4 1]
# Sample Output:

# 1
# If there are multiple possible answers ( like in the sample case above ), output any one.

# If there is no duplicate, output -1


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        B = list(A)
        for x in B:
            if B[abs(x)] > 0:
               B[abs(x)] = -B[abs(x)]
            else:
                return abs(x)

    def repeatedNumber2(self, A):  # smart!
        s = sum(A)
        n = len(A)
        missing = s - (n*(n-1))/2
        return missing