#!/usr/bin/env python3


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        stack = []
        x = 1

        while True:
            if len(stack) == k:
                res.append(stack[:])
                
            if len(stack) == k or x > n:
                if not stack:
                    return res
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1


if __name__ == "__main__":
    s = Solution()
    n = 4
    k = 2
    result = s.combine(n, k)
    print(result)
