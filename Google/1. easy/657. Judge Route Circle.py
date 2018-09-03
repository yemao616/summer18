# Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

# The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

# Example 1:
# Input: "UD"
# Output: true
# Example 2:
# Input: "LL"
# Output: false


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        h = v = 0
        for s in moves:
            if s == 'U':
                v += 1
            elif s == 'D':
                v -= 1
            elif s == 'R':
                h += 1
            else:
                h -= 1
        return (h == 0) and (v == 0)


    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
       
        return moves.count('U')==moves.count('D') and moves.count('R')==moves.count('L')