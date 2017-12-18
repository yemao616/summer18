# Remove duplicates from Sorted Array
# Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.

# Note that even though we want you to return the new length, make sure to change the original array as well in place

# Do not allocate extra space for another array, you must do this in place with constant memory.

#  Example: 
# Given input array A = [1,1,2],
# Your function should return length = 2, and A is now [1,2]. 

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) < 2:
            return len(A)
        i, j = 0, 1
        while j < len(A):
            if A[i] == A[j]:
                A.pop(i)
            else:
                i += 1
                j += 1
        return len(A)



	def removeDuplicates(self, A):
	        if len(A)<2:
	            return len(A)
	        
	        #Maintain an end pointer indicating the end of array
	        #current pointer i, that compares ith and i+1th element!
	        #If you encounter equals, end pointer need not be incremented 
	        #We append element at end and increment end if and only if
	        #i and i+1 (the elements ahead) are different , 
	        #that is whenever we encounter non repeating elements!!
	        end =0
	        #i goes from 0 to N-1 , i+1 goes from 1 to N
	        #This is because end needs to be incremented atleast once
	        for i in range(len(A)):
	            #Make sure i+1 doesn't give list index out of bounds
	            if i+1 < len(A) and A[i] == A[i+1]:
	                continue
	            #If i and i+1 have unequal elements
	            A[end] = A[i]
	            end+=1
	        
	        return end