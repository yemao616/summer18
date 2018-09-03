# You are given a string representing an attendance record for a student. The record only contains the following three characters:
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

# You need to return whether the student could be rewarded according to his attendance record.

# Example 1:
# Input: "PPALLP"
# Output: True
# Example 2:
# Input: "PPALLL"
# Output: False

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if s.count('A') <2:
            if s.count('L') < 3:
                return True
            c = 0
            for each in s:
                if each == 'L':
                    c += 1
                    if c > 2:
                        return False
                else:
                    c = 0
            return True
        return False



    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return (s.count('A') <= 1) and ('LLL' not in s)