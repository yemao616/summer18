# FizzBuzzBookmark Suggest Edit
# Problem Setter: yashpal1995 
# Problem Tester: mihai.gheorghe
# Given a positive integer N, print all the integers from 1 to N. But for multiples of 3 print “Fizz” instead of the number and for the multiples of 5 print “Buzz”. Also for number which are multiple of 3 and 5, prints “FizzBuzz”.

# Example

# N = 5
# Return: [1 2 Fizz 4 Buzz]
# Note: Instead of printing the answer, you have to return it as list of strings.


class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        ls = range(1,A+1)
        for i in xrange(3,A+1,3):
            ls[i-1] = 'Fizz'
        for i in xrange(5,A+1,5):
            ls[i-1] = 'Buzz'
        for i in xrange(15,A+1,15):
            ls[i-1] = 'FizzBuzz'
        return ls