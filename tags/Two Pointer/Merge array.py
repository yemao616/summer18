# Given two sorted integer arrays A and B, merge B into A as one sorted array.

#  Note: You have to modify the array A to contain the merge of A and B. Do not output anything in your code.
# TIP: C users, please malloc the result into a new array and return the result. 
# If the number of elements initialized in A and B are m and n respectively, the resulting size of array A after your code is executed should be m + n

# Example :

# Input : 
#          A : [1 5 8]
#          B : [6 9]

# Modified A : [1 5 6 8 9]



class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return A modified after the merge
    def merge(self, A, B):
        m, n = len(A), len(B)
        i = j = 0
        while i < m and j < n:
            if A[i] <= B[j]:
                if i == m-1:
                    A.insert(m, B[j])
                    break
                i += 1
            else:
                A.insert(i, B[j])
                j += 1
        return A


    def merge(self, A, B):
        i = j = 0
        while i < len(A) and j < len(B):
            if A[i] > B[j]:
                A.insert(i, B[j])
                j += 1
            else:
                i += 1
        if j < len(B):
            A.extend(B[j:])
        return A
            