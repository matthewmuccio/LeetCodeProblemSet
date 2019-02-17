#!/usr/bin/env python3


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None

        p = head
        q = head
        l = 1

        while p.next:
            p = p.next
            l +=1

        p.next = head
        k %= l

        for _ in range(l - k - 1):
            q = q.next

        ans = q.next
        q.next = None

        return ans


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    k = 2
    result = s.rotateRight(head, k)
    while result:
        print(result.val)
        result = result.next
