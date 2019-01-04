#!/usr/bin/env python3


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1

        if n < 0:
            n = -n
            x = 1 / x

        res = 1
        while n > 0:
            if n & 1:
                res *= x
            x *= x
            n >>= 1

        return res


if __name__ == "__main__":
    s = Solution()
    x = 2.0
    n = 10
    result = s.myPow(x, n)
    print(result)
