# Given a sorted array of integers nums and integer values a, b and c. Apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array.

# The returned array must be in sorted order.

# Expected time complexity: O(n)

# Example:
# nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,

# Result: [3, 9, 15, 33]

# nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5

# Result: [-23, -5, 1, 7]


If we plot the transformed array, it would form a parabola. 
If a > 0, the two ends will be higher than the center. 
So do a merge sort - move from both ends of the transformed array towards the center and if a > 0, 
choose the bigger element and put it at the end of the resulting array, i.e. fill the array from right to left. 
If a < 0, merge the elements from left to right.

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        ret = []
        l = 0
        r = len(nums)-1
        while l <= r:
            n_l = a*nums[l]**2 + b*nums[l] + c
            n_r = a*nums[r]**2 + b*nums[r] + c
            if a >= 0:
                if n_l >= n_r:
                    ret.append(n_l)
                    l += 1
                else:
                    ret.append(n_r)
                    r -= 1
            else:
                if n_l < n_r:
                    ret.append(n_l)
                    l += 1
                else:
                    ret.append(n_r)
                    r -= 1
        if a >= 0:
            return ret[::-1]
        return ret



        
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        nums = [x*x*a + x*b + c for x in nums]
        ret = [0] * len(nums)
        p1, p2 = 0, len(nums) - 1
        i, d = (p1, 1) if a < 0 else (p2, -1)
        while p1 <= p2:
            if nums[p1] * -d > nums[p2] * -d:
                ret[i] = nums[p1]
                p1 += 1
            else:
                ret[i] = nums[p2]
                p2 -=1
            i += d
        return ret