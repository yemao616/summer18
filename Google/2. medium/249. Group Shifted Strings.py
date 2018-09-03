# Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

# For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
# A solution is:

# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]





class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dic = collections.defaultdict(list)
        for s in strings:
            if len(s) == 1: dic[0].append(s)
            else:
                key = []
                for i in range(len(s)-1):
                    key.append((ord(s[i+1]) - ord(s[i])) % 26 )
                dic[tuple(key)].append(s)
        return dic.values()
        



class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        def diff(s):
            d = ''
            for i in xrange(1, len(s)):
                d += str((ord(s[i]) - ord(s[i-1]))%26)
            return d
        dic = collections.defaultdict(list)
        res = []
        single = []
        for s in strings:
            if len(s) > 1:
                dic[diff(s)].append(s)
            else:
                single.append(s)
        if single:
            res.append(single)
        for k, l in dic.iteritems():
            res.append(l)
        return res
        