#!/usr/bin/env python3


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0

        left = 1
        right = x

        while True:
            mid = left + (right - left) / 2

            if mid > x / mid:
                right = mid - 1
            else:
                if mid + 1 > x / (mid + 1):
                    return mid

                left = mid + 1


if __name__ == "__main__":
    s = Solution()
    x = 8
    result = s.mySqrt(x)
    print(result)
