"""
Reference: http://www.cnblogs.com/zuoyuan/p/3701639.html

~Hint:
	apply two points: fast and slow
	with cycle: fast = slow at some point, fast move two steps each time!!
	without cycle: fast achieve end earlier

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

