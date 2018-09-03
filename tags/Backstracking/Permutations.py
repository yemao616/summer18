# Given a collection of numbers, return all possible permutations.

# Example:

# [1,2,3] will have the following permutations:

# [1,2,3]
# [1,3,2]
# [2,1,3] 
# [2,3,1] 
# [3,1,2] 
# [3,2,1]
#  NOTE
# No two entries in the permutation sequence should be the same.
# For the purpose of this problem, assume that all the numbers in the collection are unique.
#  Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS.
# Example : next_permutations in C++ / itertools.permutations in python.
# If you do, we will disqualify your submission retroactively and give you penalty points. 


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        l = []
        self.backstrack(l, [], A)
        return l
        
    def backstrack(self, l, templist, nums):
        if len(templist) == len(nums):
            l.append(templist)
        else:
          for i in xrange(len(nums)):
            if nums[i] in templist:
                continue   # element already exists, skip
            self.backstrack(l, templist + [nums[i]], nums)
          