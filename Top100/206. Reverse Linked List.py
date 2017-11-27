
# Reverse a singly linked list.


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse_help(None, head)
        
        def reverse_help(self, prev, curr):
            if not curr:
                return prev
            node = curr.next
            curr.next = prev
            return self.reverse_help(curr, node)

    def reverseList2(self, head):
        prev = None
        while(head):
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev


    def reverseList3(self, head):
        stack = []
        while(head):
            stack.append(head.val)
            head = head.next
        print stack
        
        cur = dummy = ListNode(0)
        while (stack):
             cur.next = ListNode(stack.pop())
             cur = cur.next
        return dummy.next