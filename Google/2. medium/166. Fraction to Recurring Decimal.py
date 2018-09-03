# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

# If the fractional part is repeating, enclose the repeating part in parentheses.

# For example,

# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".




class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        The time complexity is generally O(denominator), but should be much smaller in fact. 
        The fraction 1 / n may have a loop sequence of at most n - 1 in length, 
        but usually far shorter. Space complexity is the same scale.
        """
        if numerator == 0:
            return "0"
        
        isNeg = (numerator ^ denominator) < 0
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        q, r = numerator // denominator, numerator % denominator
        
        if r == 0:
            return ('', '-')[isNeg] + str(q)
        
        ans = [str(q) + '.']
        table = {r: 1}
        idx = 1

        while True:
            r *= 10
            q, r = r // denominator, r % denominator
            ans.append(str(q))
            
            if r == 0:
                break
            
            if r in table:
                ans = ans[:table[r]] + ['('] + ans[table[r]:] + [')']
                break

            idx += 1
            table[r] = idx
        
        return ('', '-')[isNeg] + ''.join(ans) 