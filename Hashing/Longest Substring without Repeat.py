# Given a string, 
# find the length of the longest substring without repeating characters.

# Example:

# The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.

# For "bbbbb" the longest substring is "b", with the length of 1

class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        start = maxLength = 0
        usedChar = {}
        s = A
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength