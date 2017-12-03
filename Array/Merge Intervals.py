# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Example 1:

# Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

# Example 2:

# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

# Make sure the returned intervals are also sorted.



# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        res = []
        i = 0
        while i < len(intervals):
            s, e = new_interval.start, new_interval.end
            if s > e:
                s, e = e, s
            x = intervals[i]
            
            if x.end < s:
                res.append(x)
            elif x.start > e:
                res.append(new_interval)
                res.extend(intervals[i:])
                break
            else:
                new_interval.start, new_interval.end = min(x.start, s), max(x.end, e)
            i += 1
            
        if i == len(intervals):
            res.append(new_interval)
        return res