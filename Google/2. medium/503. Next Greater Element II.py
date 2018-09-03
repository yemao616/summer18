# Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

# Example 1:
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number; 
# The second 1's next greater number needs to search circularly, which is also 2.
# Note: The length of given array won't exceed 10000.




class Solution(object):
    def nextGreaterElements(self, nums):
        stack, res = [], [-1] * len(nums)
        for i in range(len(nums)) * 2:
            while stack and (nums[stack[-1]] < nums[i]):
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res



    def nextGreaterElements(self, nums):        # TLE on the last one
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        res = []
        ma, n = max(nums), len(nums)
        for i in xrange(n):
            if nums[i] == ma:
                res.append(-1)
            else:
                for j in xrange(i+1, i+n):
                    if nums[j%n] > nums[i]:
                        res.append(nums[j%n])
                        break
        return res