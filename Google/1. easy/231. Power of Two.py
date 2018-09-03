# Given an integer, write a function to determine if it is a power of two.


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n <= 0:
            return False
        while n > 2:
            n, r = divmod(n, 2)
            if r != 0:
                return False
        
        return True




    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        
        # num contains only one bit
        return n & (n-1) == 0