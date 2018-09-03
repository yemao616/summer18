# Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

# According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

# For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

# Note: If there are several possible values for h, the maximum one is taken as the h-index.



class Solution(object):
	def hIndex(self, citations):	# O(nlgn)
	    citations.sort()
	    n = len(citations)
	    for i in xrange(n):
	        if citations[i] >= n-i:
	            return n-i
	    return 0



	def hIndex(self, citations):	# O(n) space, O(n) time
	    n = len(citations)
	    citeCount = [0] * (n+1)
	    for c in citations:
	        if c >= n:
	            citeCount[n] += 1
	        else:
	            citeCount[c] += 1
	    
	    i = n-1
	    while i >= 0:
	        citeCount[i] += citeCount[i+1]
	        if citeCount[i+1] >= i+1:
	            return i+1
	        i -= 1
	    return 0



Further Thoughts
Is it possible to have multiple hh-values?

The answer is NO. One can find this intuitively from Figure 1. The dashed line y = xy=x crosses the histogram once and only once, because the sorted bars are monotonic. It can also be proven from the definition of the hh-index.

