# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# For example,
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3


from collections import deque
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.cache = deque()
        self.sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
    
        self.cache.append(val)
        self.sum += val
        if len(self.cache) > self.size:
            self.sum -= self.cache.popleft()
        return self.sum/float(len(self.cache))
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)