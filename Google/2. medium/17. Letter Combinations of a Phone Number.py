# Given a digit string, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below.



# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letters = {'0':' ','1':'*','2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        output = []
        
        for num in digits:
            if output:
                temp = []
                for pre in output:
                    for ch in letters[num]:
                        temp.append(pre + ch)
                output = temp
            else:
                for ch in letters[num]:
                    output.append(ch)
            
        return output



class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        def helper(digits):
            if len(digits) == 0:
                return []
            if len(digits) == 1:
                return list(mapping[digits[0]])
            prev = helper(digits[:-1])
            additional = mapping[digits[-1]]
            return [s + c for s in prev for c in additional]
        
        return helper(digits)