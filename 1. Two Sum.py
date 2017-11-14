# Refer: http://www.cnblogs.com/zuoyuan/p/3698966.html

# Hint: using Hash, wihch is dic in python instead of list alone

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = {}
        for i in range(len(nums)):
            x = nums[i]
            if target - x in ans:
                return [i, ans[target-x]]
            ans[x] = i
