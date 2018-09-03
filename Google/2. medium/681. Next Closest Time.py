# Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

# You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

# Example 1:

# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
# Example 2:

# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.



class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        digits = sorted(set(map(int, [ch for ch in time if ch != ':'])))
    
        idx1 = digits.index(int(time[4]))
        if idx1 < len(digits) -1:
            return time[:4] + str(digits[idx1+1])

        idx2 = digits.index(int(time[3]))
        if idx2 < len(digits) - 1 and digits[idx2+1] <= 5:
            return time[:3] + str(digits[idx2+1]) + str(digits[0])

        idx3 = digits.index(int(time[1]))
        if idx3 < len(digits) - 1 and int(time[0]) * 10 + digits[idx3+1] < 24:
            return time[:1] + '{0}:{1}{1}'.format(digits[idx3+1], digits[0])

        idx4 = digits.index(int(time[0]))
        if idx4 < len(digits) -1 and digits[idx4+1] <=2:
            return '{0}{1}:{1}{1}'.format(digits[idx4+1], digits[0])

        return '{0}{0}:{0}{0}'.format(digits[0])
        




from datetime import *

class Solution(object):
    def nextClosestTime(self, time):
        digits = set(time)
        while True:
            time = (datetime.strptime(time, '%H:%M') + timedelta(minutes=1)).strftime('%H:%M')
            if set(time) <= digits:
                return time