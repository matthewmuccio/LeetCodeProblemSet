#!/usr/bin/env python3


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        num = 0
        curr = head
        while curr:
            curr = curr.next
            num += 1

        group_num = num // k
        pre_group_last = ListNode(0)
        pre_group_last.next = head

        first = pre_group_last
        group_head = head

        for i in range(group_num):
            slow = group_head
            fast = slow.next
            for j in range(k - 1):
                t = fast
                fast = fast.next
                t.next = slow
                slow = t

            pre_group_last.next = slow
            pre_group_last = group_head
            pre_group_last.next = fast
            group_head = fast

        return first.next


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    k = 2

    result = s.reverseKGroup(head, k)
    while result:
        print(result.val)
        result = result.next
