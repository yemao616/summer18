# Implement an iterator to flatten a 2d vector.

# For example,
# Given 2d vector =

# [
#   [1,2],
#   [3],
#   [4,5,6]
# ]
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].




class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.cache = []
        for each in vec2d:
            self.cache += each
        self.cache = self.cache[::-1]
        
    def next(self):
        """
        :rtype: int
        """
        return self.cache.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.cache)
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())