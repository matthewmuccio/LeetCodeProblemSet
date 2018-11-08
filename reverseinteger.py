#!/usr/bin/env python3


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = int(str(abs(x))[::-1])
        if result > 2 ** 31 - 1:
            return 0
        return result if x >= 0 else 0 - result


if __name__ == "__main__":
    s = Solution()
    x = 120
    result = s.reverse(x)
    print(result)
