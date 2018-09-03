
# Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

# Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

# Could you do this in O(n) runtime?

# Example:

# Input: [3, 10, 5, 25, 2, 8]

# Output: 28

# Explanation: The maximum result is 5 ^ 25 = 28.



"""
key idea: answer += any(answer^1 ^ p in prefixes for p in prefixes)
if (answer^1) XOR p matches Z in prefixes, then p XOR Z matches (answer^1), 
which is what I am looking for. p and Z are both elements in the prefix set."""

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        for i in range(32)[::-1]:
            answer <<= 1
            prefixes = {num >> i for num in nums}
            
            for p in prefixes:
                if answer^1 ^ p in prefixes:
                    answer += 1
                    break
        return answer