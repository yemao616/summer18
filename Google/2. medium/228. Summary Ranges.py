# Given a sorted integer array without duplicates, return the summary of its ranges.

# Example 1:
# Input: [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Example 2:
# Input: [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]



class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        res = []
        nums = nums + [float('inf')]
        lo = high = nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                high = nums[i]
            else:
                if lo == high:
                    res.append(str(lo))
                else:
                    res.append(str(lo) + '->' + str(high))
                lo = high = nums[i]
        return res
            