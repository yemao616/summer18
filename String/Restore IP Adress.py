# Valid Ip AddressesBookmark Suggest Edit
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.

# A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.

# Example:

# Given “25525511135”,

# return [“255.255.11.135”, “255.255.111.35”]. (Make sure the returned strings are sorted in order)

class Solution:
    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, A):
        ans = []
        self.helper(ans, A, 4, [])
        return ['.'.join(x) for x in ans]
        
    def helper(self, ans, s, k, temp):
        if len(s) > k*3:
            return
        if k == 0:
            ans.append(temp[:])
        else:
            for i in range(min(3,len(s)-k+1)):
                if i==2 and int(s[:3]) > 255 or i > 0 and s[0] == '0':
                    continue
                self.helper(ans, s[i+1:], k-1, temp+[s[:i+1]])