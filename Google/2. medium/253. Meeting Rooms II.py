# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.



# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        e = ret = 0
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)
        print start, end
        for s in start:
            if s < end[e]:  # e is a pointer to the first available room
                ret += 1
            else: 
                e += 1
        return ret
                