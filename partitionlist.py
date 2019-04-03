#!/usr/bin/env python3


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        head1 = l1 = ListNode(0)
        head2 = l2 = ListNode(0)
        
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
                
            head = head.next
            
        l2.next = None
        l1.next = head2.next
        
        return head1.next


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)
    x = 3
    result = s.partition(head, x)
    while result:
        print(result.val)
        result = result.next
