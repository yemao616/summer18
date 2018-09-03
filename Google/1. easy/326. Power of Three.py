# Given an integer, write a function to determine if it is a power of three.

# Follow up:
# Could you do it without using any loop / recursion?


class Solution(object):
    def isPowerOfThree(self, n):
        return n > 0 and 1162261467 % n == 0 		# max power of 3



    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
          
        return (math.log10(n) / math.log10(3)) % 1 == 0


    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1


