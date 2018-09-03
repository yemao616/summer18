# Merge k sorted linked lists and return it as one sorted list.

# Example :

# 1 -> 10 -> 20
# 4 -> 11 -> 13
# 3 -> 8 -> 9
# will result in

# 1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20






# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):                
        dummy=Node=ListNode(0)
        heap=[(node.val,node) for node in A if node]
        heapq.heapify(heap)
        while heap :
            
            v , n = heap[0]
            
            if n.next is None :
                heapq.heappop(heap)
            
            else :
                heapq.heapreplace(heap,(n.next.val,n.next))
            Node.next=n
            Node=Node.next
        return dummy.next   

Close




    def mergeKLists(self, A):
        s = []
        for each in A:
            while each:
                s.append(each.val)
                each = each.next
        s.sort()
        curr = dummy = ListNode(None)
        for x in s:
            curr.next = ListNode(x)
            curr = curr.next
        return dummy.next