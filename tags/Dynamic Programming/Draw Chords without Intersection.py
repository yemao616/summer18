# Given a number N, return number of ways you can draw N chords in a circle with 2*N points such that no 2 chords intersect.
# Two ways are different if there exists a chord which is present in one way and not in other.

# For example,

# N=2
# If points are numbered 1 to 4 in clockwise direction, then different ways to draw chords are:
# {(1-2), (3-4)} and {(1-4), (2-3)}

# So, we return 2.
# Notes:

# 1 ≤ N ≤ 1000
# Return answer modulo 109+7.



# Think in terms of DP.
# Can we relate answer for N with smaller answers.

# If we draw a chord between any two points, can you observe current set of points getting broken into two smaller sets S_1 and S_2? Can a chord be drawn between two points where each point belong to different set?

# If we draw a chord from a point in S_1 to a point in S_2, it will surely intersect the chord we’ve just drawn.

# So, we can arrive at a recurrence that Ways(n) = sum[i = 0 to n-1] { Ways(i)*Ways(n-i-1) }.
# Here we iterate over i, assuming that size of one of the sets is i and size of other set automatically is (n-i-1) since we’ve already used a pair of points and i pair of points in one set.



class Solution:
    # @param A : integer
    # @return an integer
    def chordCnt(self,N):
        mod = 1000000007
        if N < 2:
            return 1
        f = [0 for i in xrange(N + 1)]
        f[0], f[1] = 1, 1
    
        for i in xrange(2, N + 1):
            lenx = 0
            if i & 1:
                lenx = i / 2 + 1
            else:
                lenx = i / 2
    
            for j in xrange(0, lenx):
                if j == i - j - 1:
                    f[i] = (f[i] + f[j] * f[j]) % mod
                else:
                    f[i] = (f[i] + f[j] * f[i - j - 1] * 2) % mod
    
        return f[N] % mod



    def chordCnt(self, A):
        if A<0:
            return 0
        if A<2:
            return 1
        ans=1
        i=2
        for i in range(2,A+1):
            ans=((ans*2*(2*i-1))/(i+1))
        return (ans%1000000007)