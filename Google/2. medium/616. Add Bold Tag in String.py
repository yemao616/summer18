# Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
# Example 1:
# Input: 
# s = "abcxyz123"
# dict = ["abc","123"]
# Output:
# "<b>abc</b>xyz<b>123</b>"
# Example 2:
# Input: 
# s = "aaabbcc"
# dict = ["aaa","aab","bc"]
# Output:
# "<b>aaabbc</b>c"
# Note:
# The given dict won't contain duplicates, and its length won't exceed 100.
# All the strings in input have length in range [1, 1000].


class Solution(object):
    def addBoldTag(self, S, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        paint = [False] * len(S)
        for i in xrange(len(S)):
            block = S[i:]
            for word in dict:
                if block.startswith(word):
                    paint[i:i+len(word)] = [True] * len(word)

        ans = []
        for i, u in enumerate(S):
            if paint[i] and (i == 0 or not paint[i-1]):
                ans.append('<b>')
            ans.append(u)
            if paint[i] and (i == len(S) - 1 or not paint[i+1]):
                ans.append('</b>')

        return "".join(ans)




    def addBoldTag(self, s, dict):
        
        def mergeInterval(indexes):
            start, end = 0, 0
            n = len(indexes)
            while end < n:
                indexes[start] = indexes[end]
                while end < n and indexes[end][0] <= indexes[start][1]:
                    indexes[start][1] = max(indexes[start][1], indexes[end][1])
                    end += 1
                start += 1
            del indexes[start:]

        # find all overlapping matches
        matches = []
        for word in dict:
            start = 0
            while True:
                start = s.find(word, start)
                if start == -1:
                    break
                else:
                    matches.append([start, start + len(word)])
                    start += 1

        # merge all matches like indexes
        matches.sort()
        mergeInterval(matches)

        # concatenate string
        ret = ""
        pos = 0
        for start, end in matches:
            ret += s[pos:start] + '<b>' + s[start:end] + '</b>'
            pos = end
        ret += s[pos:]
        return ret