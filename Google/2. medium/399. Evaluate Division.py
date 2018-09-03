# Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

# Example:
# Given a / b = 2.0, b / c = 3.0. 
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].

# The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

# According to the example above:

# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
# The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.


class Solution(object):
    def calcEquation(self, equations, values, queries):		# floy algrithm
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        cal = collections.defaultdict(dict)
        for (a, b), val in zip(equations, values):
            cal[a][b] = val
            cal[a][a] = cal[b][b] = 1.0
            cal[b][a] = 1/val
        for k in cal:
            for i in cal[k]:
                for j in cal[k]:
                    cal[i][j] = cal[i][k]*cal[k][j]
        return [cal[a].get(b, -1.0) for a, b in queries]