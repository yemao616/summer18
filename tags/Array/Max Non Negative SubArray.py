# Find out the maximum sub-array of non negative numbers from an array.
# The sub-array should be continuous. That is, a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

# Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).

# Example:

# A : [1, 2, 5, -7, 2, 3]
# The two sub-arrays are [1, 2, 5] [2, 3].
# The answer is [1, 2, 5] as its sum is larger than [2, 3]
# NOTE: If there is a tie, then compare with segment's length and return segment which has maximum length
# NOTE 2: If there is still a tie, then return the segment with minimum starting index



class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        i = j = -1
        start = cur_sum = max_sum = 0
        for ind, each in enumerate(A):
            cur_sum += each
            if each < 0:
                start = ind+1
                cur_sum = 0

            elif cur_sum > max_sum or (cur_sum == max_sum and ind-start>j-i):
                max_sum, i, j = cur_sum, start, ind
            
        if i == -1:
            return []
        return A[i:j+1]


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        a = b = num = lens = -1
        res = lens = []
        n = len(A)
        for i in xrange(n):
            if A[i]>=0:
                if b == -1:
                    b = a = i
                else:    
                    b += 1
            else:
                end = min(b+1, n)
                res.append(A[a:end])
                lens.append(sum(A[a:end]))
                b = -1

        # insert last group
        end = min(b+1, n)
        res.append(A[a:end])
        lens.append(sum(A[a:end]))

        return res[lens.index(max(lens))]



import collections
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        start = end = 0
        cur_sum = max_sum = 0
        tmp = collections.defaultdict(list)
        for i, each in enumerate(A):
            if each < 0:
                tmp[cur_sum].append((start, i-1))
                start = i+1
                cur_sum = 0
                continue
            cur_sum += each
            if cur_sum > max_sum:
                max_sum = cur_sum
            if i == len(A)-1:
                tmp[cur_sum].append((start, i))
        i, j = tmp[max_sum][0]
        return A[i:j+1]