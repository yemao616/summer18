# Divide two integers without using multiplication, division and mod operator.

# Return the floor of the result of the division.

# Example:

# 5 / 2 = 2
# Also, consider if there can be overflow cases. For overflow case, return INT_MAX.


def divide(self, x, y):
        result = 0
        is_neg = (x < 0) ^ (y < 0)
        x, y = abs(x), abs(y)
        power = 0
        y_power = y << power
        
        while y_power <= x:
            power += 1
            y_power = y << power
            
        while x >= y:
            while y_power > x:
                y_power >>= 1
                power -= 1
                
            result += (1 << power)
            x -= y_power
            
        result = result if is_neg == False else -result
        return min(result, 2147483647)