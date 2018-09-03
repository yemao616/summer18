# Design and implement a data structure for a compressed string iterator. It should support the following operations: next and hasNext.

# The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.

# next() - if the original string still has uncompressed characters, return the next letter; Otherwise return a white space.
# hasNext() - Judge whether there is any letter needs to be uncompressed.

# Note:
# Please remember to RESET your class variables declared in StringIterator, as static/class variables are persisted across multiple test cases. Please see here for more details.

# Example:

# StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");

# iterator.next(); // return 'L'
# iterator.next(); // return 'e'
# iterator.next(); // return 'e'
# iterator.next(); // return 't'
# iterator.next(); // return 'C'
# iterator.next(); // return 'o'
# iterator.next(); // return 'd'
# iterator.hasNext(); // return true
# iterator.next(); // return 'e'
# iterator.hasNext(); // return false
# iterator.next(); // return ' '




import re
class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        tmp = re.findall(r'[a-zA-Z][0-9]+', compressedString)
        self.ss = [[x[0], int(x[1:])] for x in tmp]
        

    def next(self):
        """
        :rtype: str
        """
        if len(self.ss) == 0:
            return ' '
        rv = self.ss[0][0]
        self.ss[0][1] -= 1
        if self.ss[0][1] == 0:
            self.ss.pop(0)
        return rv
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.ss) > 0



class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.ind = 0
        self.string = []
        tmp, c ='', ''
        for i in xrange(len(compressedString)):
            s = compressedString[i]
            if s.isalpha():
                if tmp and c:
                    self.string.append([tmp, int(c)])
                    i += 1
                    c = ''
                tmp = s
            else:
                c += s
        self.string.append([tmp, int(c)])
        print self.string
       
    def next(self):
        """
        :rtype: str
        """
        if self.hasNext():
            self.string[self.ind][1] -= 1
            return self.string[self.ind][0]
        else:
            return ' '
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.string[self.ind][1] > 0:
            return True
        elif self.ind < len(self.string)-1:
            self.ind += 1
            return True
        else:
            return False