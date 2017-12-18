# Given a singly linked list and an integer K, reverses the nodes of the

# list K at a time and returns modified linked list.

#  NOTE : The length of the list is divisible by K 
# Example :

# Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,

# You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5

# Try to solve the problem using constant extra space.





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        if B <= 1 or A is None or A.next is None:
            return A
        newHead = ListNode(0)
        newHead.next = A
        tail = prev = newHead
        start = prev.next
        while True:           
            for i in xrange(B):
                tail = tail.next
                if tail is None:
                    return newHead.next

            for i in xrange(B-1):
                then = start.next
                start.next = then.next
                then.next = prev.next
                prev.next = then
                
            tail = prev = start
            start = prev.next




class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        if B == 1: return A
        current = A
        prev_tail = None
        new_list_head = None
        while current is not None:
            new_head, new_tail, current = self.reverseK(current, B)
            if prev_tail is not None:
                prev_tail.next = new_head
            if new_list_head is None:
                new_list_head = new_head
            prev_tail = new_tail
        return new_list_head
            
        
    def reverseK(self, node, k):
        tail = node
        current = node
        prev = None
        while k > 0:
            next = current.next
            current.next = prev
            prev = current
            current = next
            k -= 1
        return prev, tail, current # head, tail, next_start