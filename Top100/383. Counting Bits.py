# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

# Example:
# For num = 5 you should return [0,1,1,2,1,2].

# Follow up:

# It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        total = []
        for n in xrange(num+1):
            total.append(bin(n).count('1'))
            
        return total


    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]*(num + 1)
        for i in xrange(1, num+1):
            ans[i] = ans[i & (i - 1)] + 1
        return ans