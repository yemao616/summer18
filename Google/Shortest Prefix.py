# Find shortest unique prefix to represent each word in the list.

# Example:

# Input: [zebra, dog, duck, dove]
# Output: {z, dog, du, dov}
# where we can see that
# zebra = z
# dog = dog
# duck = du
# dove = dov
#  NOTE : Assume that no word is prefix of another. In other words, the representation is always possible. 



class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        tree = [0, {}]
        for s in A:
            node = tree
            node[0] += 1
            for c in s:
                node = node[1].setdefault(c, [0, {}])
                node[0] += 1
        l = []
        for s in A:
            prefix = ''
            node = tree
            for c in s:
                if node[0] <= 1:
                    l.append(prefix)
                    break
                prefix += c
                node = node[1][c]
            else:
                l.append(s)
        return l