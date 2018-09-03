# Implement pow(x, n).


# Example 1:

# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:

# Input: 2.10000, 3
# Output: 9.26100


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if n == 0:
            return 1
        ans = 1
        square = x
        flag = 0
        if n < 0:
            flag = 1
            n = -n
        while n:
            if n % 2:
                ans *= square
            square = square * square
            n = n / 2
        if flag:
            ans = 1/float(ans)
        return ans