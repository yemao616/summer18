# The set [1,2,3,…,n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3 ) :

# 1. "123"
# 2. "132"
# 3. "213"
# 4. "231"
# 5. "312"
# 6. "321"
# Given n and k, return the kth permutation sequence.

# For example, given n = 3, k = 4, ans = "231"

#  Good questions to ask the interviewer :
# What if n is greater than 10. How should multiple digit numbers be represented in string?
#  In this case, just concatenate the number to the answer.
# so if n = 11, k = 1, ans = "1234567891011" 
# Whats the maximum value of n and k?
#  In this case, k will be a positive integer thats less than INT_MAX.
# n is reasonable enough to make sure the answer does not bloat up a lot.

class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def getPermutation(self, A, B):
        res, mul = '', 1
        fac = [1]
        num = []
        k = B-1
        for i in xrange(1,A+1):
            mul *= i
            fac.append(mul)      # fac records the factorial
            num.append(i)		# num record the digits
        for i in xrange(1, A+1):
            temp = fac[A-i]
            ind = k/temp
            res += str(num[ind])
            num.pop(ind)
            k -= ind*temp
        return res
