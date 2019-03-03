#!/usr/bin/env python3


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, 1

        for i in range(n):
            a, b = b, a + b

        return a


if __name__ == "__main__":
    s = Solution()
    n = 3
    result = s.climbStairs(n)
    print(result)
