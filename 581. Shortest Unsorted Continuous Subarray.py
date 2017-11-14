"""
Reference: http://bookshadow.com/weblog/2017/05/15/leetcode-shortest-unsorted-continuous-subarray/

~Hint: use two numbers to record the first and last index

"""



class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        snum = sorted(nums)
        a = b = -1
        for i in range(len(nums)):
            if snum[i] != nums[i]:
                if a == -1:
                    a = i
                b = i
        if a == b:
            return 0
        else:
            return b-a+1
