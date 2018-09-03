# Write a program to find the nth super ugly number.

# Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

# Note:
# (1) 1 is a super ugly number for any given primes.
# (2) The given numbers in primes are in ascending order.
# (3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
# (4) The nth super ugly number is guaranteed to fit in a 32-bit signed integer.



# 这道题是之前那道Ugly Number 丑陋数的延伸，这里让我们找到第n个丑陋数，还好题目中给了很多提示，基本上相当于告诉我们解法了，根据提示中的信息，我们知道丑陋数序列可以拆分为下面3个子列表：

# (1) 1x2,  2x2, 2x2, 3x2, 3x2, 4x2, 5x2...
# (2) 1x3,  1x3, 2x3, 2x3, 2x3, 3x3, 3x3...
# (3) 1x5,  1x5, 1x5, 1x5, 2x5, 2x5, 2x5...


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [1] * n
	    i_list = [-1] * len(primes)     # i[ind] records the index in ugly to multiply primes[ind]
	    v_list = [1] * len(primes)      # v[ind] records the value of multiplication
	    k = 0
	    while k < n:
	        x = min(v_list)
	        ugly[k] = x
	        for v in xrange(len(v_list)):
	            if x == v_list[v]:
	                i_list[v] += 1
	                v_list[v] = ugly[i_list[v]] * primes[v]
	        k += 1
	    return ugly[k - 1]
            
            