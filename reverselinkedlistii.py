#!/usr/bin/env python3


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n: return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode

        for i in range(m - 1):
            pre = pre.next
        
        reverse = None
        curr = pre.next
        
        for i in range(n - m + 1):
            next = curr.next
            curr.next = reverse
            reverse = curr
            curr = next

        pre.next.next = curr
        pre.next = reverse

        return dummyNode.next


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    m = 2
    n = 4
    result = s.reverseBetween(head, m, n)
    while result:
        print(result.val)
        result = result.next
