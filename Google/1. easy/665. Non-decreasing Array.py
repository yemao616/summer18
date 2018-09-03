# Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

# Example 1:
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# Example 2:
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one element.
# Note: The n belongs to [1, 10,000].


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        one, two = nums[:], nums[:]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                one[i] = nums[i + 1]
                two[i + 1] = nums[i]
                break
        return one == sorted(one) or two == sorted(two)




    def checkPossibility(self, nums):
    # greedy, find i with nums[i-1]>nums[i]
    # modify nums[i-1] or nums[i], e.g, [3,4,2,3]
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                cnt += 1
                if i < 2 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i] # modify nums[i-1]
                else:
                    nums[i] = nums[i - 1] # modify nums[i]
        return cnt <= 1