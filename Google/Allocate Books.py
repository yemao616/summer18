# N number of books are given. 
# The ith book has Pi number of pages. 
# You have to allocate books to M number of students so that maximum number of pages alloted to a student is minimum. A book will be allocated to exactly one student. Each student has to be allocated at least one book. Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.

# NOTE: Return -1 if a valid assignment is not possible

# Input:

# List of Books
# M number of students
# Your function should return an integer corresponding to the minimum number.

# Example:

# P : [12, 34, 67, 90]
# M : 2

# Output : 113

# There are 2 number of students. Books can be distributed in following fashion : 
#   1) [12] and [34, 67, 90]
#       Max number of pages is allocated to student 2 with 34 + 67 + 90 = 191 pages
#   2) [12, 34] and [67, 90]
#       Max number of pages is allocated to student 2 with 67 + 90 = 157 pages 
#   3) [12, 34, 67] and [90]
#       Max number of pages is allocated to student 1 with 12 + 34 + 67 = 113 pages

# Of the 3 cases, Option 3 has the minimum pages = 113. 

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        if B > len(A):
            return -1
        start = max(A)
        end = sum(A)
        res = -1
        while start <= end:
            mid = (start + end) / 2
            if self.required_students(A, mid) <= B:
                res = mid
                end = mid-1
            else:
                start = mid+1
        return res
            
    def required_students(self, l, pages_per_student):
        n, total = 1, 0
        for i in xrange(len(l)):
            total += l[i]
            if total > pages_per_student:
                total = l[i]
                n += 1
        return n