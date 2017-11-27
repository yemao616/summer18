# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
            """
        left = 0
        cur = head = ListNode(0)
        while l1 or l2:
            val = left
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            current, left = val%10, val/10
            cur.next = ListNode(current)
            cur = cur.next
            
        if left != 0:
            cur.next = ListNode(left)
        return head.next