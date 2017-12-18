# Find the largest continuous sequence in a array which sums to zero.

# Example:


# Input:  {1 ,2 ,-2 ,4 ,-4}
# Output: {2 ,-2 ,4 ,-4}




class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        seen_sums = dict()
        sm = 0
        strt, end = 0,0
        seen_sums[0] = 0
        for idx, a in enumerate(A,1):
            sm += a
            if sm in seen_sums:
                if end-strt < idx - seen_sums[sm]:
                    strt, end = seen_sums[sm], idx
            else:
                seen_sums[sm] = idx

        return A[strt:end] if strt != end else []