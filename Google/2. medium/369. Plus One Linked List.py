# Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

# You may assume the integer do not contain any leading zero, except the number 0 itself.

# The digits are stored such that the most significant digit is at the head of the list.

# Example:
# Input:
# 1->2->3

# Output:
# 1->2->4

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = list()
        curt = head
        while curt:
            stack.append(curt)
            curt = curt.next
        carry = 1
        while stack:
            node = stack.pop()
            su = node.val + carry
            carry = su / 10
            node.val = su % 10
        if carry:
            node = ListNode(1)
            node.next = head
            head = node
        return head




    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = ''
        while head:
            s += str(head.val)
            head = head.next
        s = str(int(s)+1)
        dummy = curr = ListNode(0)
        for each in s:
            curr.next = ListNode(int(each))
            curr = curr.next
        return dummy.next