#!/usr/bin/env python3


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = curr = ListNode(0)

        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next

        for x in sorted(self.nodes):
            curr.next = ListNode(x)
            curr = curr.next

        return head.next


if __name__ == "__main__":
    s = Solution()
    node1 = ListNode(1)
    node1.next = ListNode(4)
    node1.next.next = ListNode(5)
    node2 = ListNode(1)
    node2.next = ListNode(3)
    node2.next.next = ListNode(4)
    node3 = ListNode(2)
    node3.next = ListNode(6)
    lists = [node1, node2, node3]

    result = s.mergeKLists(lists)
    while result:
        print(result.val)
        result = result.next
