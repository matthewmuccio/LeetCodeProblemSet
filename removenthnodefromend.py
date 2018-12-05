#!/usr/bin/env python3


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr = head

        for _ in range(n):
            curr = curr.next
        end = head

        if curr == None:
            return head.next

        while curr.next != None:
            curr = curr.next
            end = end.next
        end.next = end.next.next

        return head


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    n = 2
    result = s.removeNthFromEnd(head, n)
    print(result)
