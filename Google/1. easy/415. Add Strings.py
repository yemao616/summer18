# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

# Note:

# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.




class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        res = ''
        carry, zero = 0, ord('0')
        while num1 or num2:
            val = carry
            if num1:
                val += ord(num1[-1]) - zero
                num1 = num1[:-1]
            if num2:
                val += ord(num2[-1]) - zero
                num2 = num2[:-1]
            carry = val/10
            res = str(val%10) + res
        if carry:
            res = str(carry) + res
        return res
            