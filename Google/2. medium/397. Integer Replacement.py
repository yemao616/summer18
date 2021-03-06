
# Given a positive integer n and you can do operations as follow:

# If n is even, replace n with n/2.
# If n is odd, you can replace n with either n + 1 or n - 1.
# What is the minimum number of replacements needed for n to become 1?

# Example 1:

# Input:
# 8

# Output:
# 3

# Explanation:
# 8 -> 4 -> 2 -> 1
# Example 2:

# Input:
# 7

# Output:
# 4

# Explanation:
# 7 -> 8 -> 4 -> 2 -> 1
# or
# 7 -> 6 -> 3 -> 2 -> 1



class Solution(object):
    def integerReplacement(self, n):        # O(lgN) time
        ctn = 0
        while n > 1:
            ctn += 1
            if n % 2 == 0:
                n //= 2
            elif n == 3 or n&2 !=2:  
                n -= 1
            else:
                n += 1  # the digit before last one is 1, then add 1 can lead to better result, except for 3
        return ctn