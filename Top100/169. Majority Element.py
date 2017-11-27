# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

class Solution(object):
	 def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate, count = None, 0
        for e in nums:
            if count == 0:
                candidate, count = e, 1
            elif e == candidate:
                count += 1
            else:
                count -= 1
            # print "e: " + str(e)+ ", candidate: "+str(candidate) + ", count: "+ str(count)
        return candidate

    def majorityElement(self, nums):
        cnt = collections.Counter(nums)
        return cnt.most_common(1)[0][0]

# NOTE: only one majority element!