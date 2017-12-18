# Given three sorted arrays A, B and Cof not necessarily same sizes.

# Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c such that a, b, c belongs arrays A, B, C respectively.
# i.e. minimize | max(a,b,c) - min(a,b,c) |.

# Example :

# Input:

# A : [ 1, 4, 5, 8, 10 ]
# B : [ 6, 9, 15 ]
# C : [ 2, 3, 6, 6 ]
# Output:

# 1
# Explanation: We get the minimum difference for a=5, b=6, c=6 as | max(a,b,c) - min(a,b,c) | = |6-5| = 1.



class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        a = b = c = 0
        ans_a = ans_b = ans_c = 0
        dis = 2**31
        while a < len(A) and b < len(B) and c < len(C):
            max_ = max(A[a], B[b], C[c])
            min_ = min(A[a], B[b], C[c])
            if max_-min_ < dis:
                ans_a, ans_b, ans_c = a, b, c
                dis = max_ - min_
            if min_ == A[a]:
                a += 1
            elif min_ == B[b]:
                b += 1
            else:
                c += 1
        return dis