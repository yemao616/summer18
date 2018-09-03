# Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.

# Example 1:
# Given points = [[1,1],[-1,1]], return true.

# Example 2:
# Given points = [[1,1],[-1,-1]], return false.

# Follow up:
# Could you do better than O(n2)?





class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
       
        n = len(points)
        if n <= 1: return True
        min_x = max_x = points[0][0]
        s = set()
        
        for p in points:
            min_x = min(min_x, p[0])
            max_x = max(max_x, p[0])
            s.add((p[0], p[1]))
            
        total = min_x + max_x
        for x, y in points:
            if (total - x, y) not in s:
                return False
            
        return True
        



class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
       
        if not points: 
            return True
        X = min(points)[0] + max(points)[0]
        return {(x, y) for x, y in points} == {(X - x, y) for x, y in points}