# Given two numbers represented as strings, return multiplication of the numbers as a string.

#  Note: The numbers can be arbitrarily large and are non-negative.
# Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer. 
# For example, 
# given strings "12", "10", your answer should be “120”.


class Solution:
    def multiply_by_digit(self, x, digit):
        carry = 0
        answer = []
        for x_i in reversed(x):
            result = int(x_i) * int(digit) + carry
            answer.append(str(result % 10))
            carry = int(result // 10)
        
        if carry != 0:
            answer.append(str(carry))  
        
        return ''.join(reversed(answer))
        
    def sum_two_numbers(self, x_1, x_2):
        # pad
        max_len = max(len(x_1), len(x_2))
        x_1 = '0' * (max_len - len(x_1)) + x_1
        x_2 = '0' * (max_len - len(x_2)) + x_2
        
        carry = 0
        answer = []
        for digit_1, digit_2 in reversed(zip(x_1, x_2)):
            result = int(digit_1) + int(digit_2) + carry
            answer.append(str(result % 10))
            carry = int(result // 10)
            
        if carry != 0:
            answer.append(str(carry))  
        
        return ''.join(reversed(answer))
            
        
    def multiply(self, x_1, x_2):
        x_1 = x_1.strip()
        x_2 = x_2.strip()
        
        min_x = min([x_1, x_2], key=int)
        max_x = max([x_1, x_2], key=int)
        
        answer = ''
        for i, min_x_i in enumerate(reversed(min_x)):
            result = self.multiply_by_digit(max_x, min_x_i) + '0' * i
            answer = self.sum_two_numbers(answer, result)
        
        # strip 0
        i = 0
        while i < len(answer) - 1 and answer[i] == '0':
            i += 1
        
        return answer[i:]