# Given two 1d vectors, implement an iterator to return their elements alternately.

# For example, given two 1d vectors:

# v1 = [1, 2]
# v2 = [3, 4, 5, 6]
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].

# Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

# Clarification for the follow up question - Update (2015-09-18):
# The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example, given the following input:

# [1,2,3]
# [4,5,6,7]
# [8,9]
# It should return [1,4,8,2,5,9,3,6,7].


from collections import deque
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.d1 = deque(v1)
        self.d2 = deque(v2)
        self.flag = 0

    def next(self):
        """
        :rtype: int
        """
        if not self.d1 and self.d2:
            return self.d2.popleft()
        elif not self.d2 and self.d1:
            return self.d1.popleft()
        elif self.flag == 0 and self.d1:
            self.flag = 1
            return self.d1.popleft()
        elif self.flag == 1 and self.d2:
            self.flag = 0
            return self.d2.popleft()
        
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.d1 or self.d2:
            return  True
        return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())




class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.vals = [x
                     for v in itertools.izip_longest(v1, v2)
                     for x in v
                     if x is not None][::-1]
   

    def next(self):
        """
        :rtype: int
        """
        return self.vals.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.vals)
