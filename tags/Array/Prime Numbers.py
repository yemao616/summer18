
# Given a number N, find all prime numbers upto N ( N included ).

# Example:

# if N = 7,

# all primes till 7 = {2, 3, 5, 7}

# Make sure the returned array is sorted.


class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        num = []
        if A < 2: return []
        if A %2 == 0:
                A -= 1
        while A >2:
            if A == 3:
                num.append(3)
            elif A >3:
                f = 0
                for i in xrange(3,int(A**0.5)+1, 2):
                    if A % i == 0:
                        f = 1
                        break
                if f == 0:
                    num.append(A)
            A -=2
        num.append(2)
        num.reverse()
        return num


	def sieve2(n):
	    sieve = [True] * (n+1)
	    for i in xrange(3, int(n**0.5)+1, 2):
	        if sieve[i]:
	            sieve[i*i::2*i] = [False]*((n-i*i)/(2*i)+1)
	    s = [2] + [i for i in xrange(3, n+1, 2) if sieve[i]]
	    return s


    class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, n):
        # Sieve of Eratosthenes
        prime = [True]*(n+1)
        p =2
        lis=[]
        while(p*p <n):
            if (prime[p] == True):
                for i in range(p*2,n+1,p):
                    prime[i] = False
            p +=1
        for i in range(2,n):
            if prime[i]:
                lis.append(i)

        return lis
        
