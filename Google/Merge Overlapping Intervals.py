# iven a collection of intervals, merge all overlapping intervals.

# For example:

# Given [1,3],[2,6],[8,10],[15,18],

# return [1,6],[8,10],[15,18].

# Make sure the returned intervals are sorted.


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        res = []
        if not intervals:
            return res
        intervals = sorted(intervals, key=lambda i: i.start)
        x = intervals[0]
        j = 1
        while j < len(intervals):
            y = intervals[j]
            if x.end < y.start:
                res.append(x)
                x = y
            elif x.start > y.end:
                res.extend(intervals[j:])
                break
            else:
                x.start, x.end = min(x.start, y.start), max(x.end, y.end)
            j += 1
    
        if j == len(intervals):
            res.append(x)
        return res



    def merge(self, intervals):
        A = intervals
        A.sort(key=lambda x: x.start)
        N = len(A)
        S = []
        if A:
            S.append(A[0])
            for i in range(1, N):
                B = A[i]
                if B.start <= S[-1].end:
                    S[-1].end = max(S[-1].end, B.end)
                else:
                    S.append(B)
        return S