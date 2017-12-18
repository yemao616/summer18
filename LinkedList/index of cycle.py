# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# Try solving it using constant additional space.

# Example :

# Input : 

#                   ______
#                  |     |
#                  \/    |
#         1 -> 2 -> 3 -> 4

# Return the node corresponding to node 3. 




class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        if A is None: return
        
        dummy = ListNode("dummy")
        current = A
        while current.next is not dummy:
            next = current.next
            if next is None: return
            current.next = dummy
            current = next
            
        return current

    def detectCycle(self, A):
        if A == None or A.next == None:
            return 
        slow = fast = A
        iscycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                iscycle = True
                break
        if iscycle:
        	fast = A
        	while slow != fast:
        		slow = slow.next
        		fast = fast.next
        	return fast