# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

# For example:

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 


class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        num = total = 0
        ref = [0]
        while A > total:
            num += 1
            total += (26**num)
            ref.append(total)
        
        s = ''
        while num:
            temp = 26**(num-1)
            red = A / temp
            A = A % temp
            if num >1 and A <= ref[num-2]:
                red -= 1
                A += temp
            s += chr(ord('A')+red-1)
            num -= 1
        return s

    def convertToTitle2(self, A):
        s = ''
        while A:
            A -= 1      ####### smart!
            red = A % 26
            A = A / 26
            s = chr(ord('A')+red) + s
        return s