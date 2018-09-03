# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Write a function to determine if a number is strobogrammatic. The number is represented as a string.

# For example, the numbers "69", "88", and "818" are all strobogrammatic.



class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        ref = set('01689')
        def transform(num):
            trans = ''
            for each in num[::-1]:
                if each == '0':
                    trans += '0'
                elif each == '6':
                    trans += '9'
                elif each == '9':
                    trans += '6'
                elif each == '8':
                    trans += '8'
                elif each == '1':
                    trans += '1'
            return num == trans
                
        if set(str(num)) - ref:
            return False
        else:
            return transform(str(num))
        

    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        l, r = 0, len(num)-1
        while l <= r:
            if num[l] in ['0', '1', '8'] and num[r] in ['0', '1', '8'] and num[l] == num[r]:
                l += 1
                r -= 1
            elif (num[l] == '6' and num[r] == '9') or (num[l] == '9' and num[r] == '6'):
                l += 1
                r -= 1
            else:
                return False
        return True