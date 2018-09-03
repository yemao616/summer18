# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Examples:

#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack = []
        for each in A:
            # if each != '+' and each != '-' and each != '*' and each != '/':
            if each.isdigit() or (each.startswith("-") and each[1:].isdigit()):
                stack.append(int(each))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if each == '+':
                    rs = op1+op2
                elif each == '-':
                    rs = op1-op2
                elif each == '*':
                    rs = op1*op2
                else:
                    rs = op1/op2
                stack.append(rs)
        return stack.pop()