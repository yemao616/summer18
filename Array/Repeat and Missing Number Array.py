# You are given a read only array of n integers from 1 to n.

# Each integer appears exactly once except A which appears twice and B which is missing.

# Return A and B.

# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Note that in your output A should precede B.

# Example:

# Input:[3 1 2 5 3] 

# Output:[3, 4] 

# A = 3, B = 4


def repeatedNumber2(A):
    temp = [-1]
    n = len(A)
    temp.extend([0]*n)
    print temp
    dup = -1
    for x in A:
        if temp[x] == 0:
            temp[x] = 1
            print temp[x]
        elif temp[x] == 1:
            dup = x
    return [dup, temp.index(0)]

def repeatedNumber(A):
    dup = mis = -100
    B = list(A)
    print B
    for x in B:
        if B[abs(x) - 1] > 0:
            B[abs(x) - 1] = -B[abs(x) - 1]
            print B[abs(x) - 1]
        else:
            dup = abs(x)
    for i in xrange(len(B)):
        if B[i] > 0:
            mis = i + 1
            break
    return [dup, mis]