#!/usr/bin/env python3


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1

        negative = False

        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            negative = True

        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= (temp << 1):
                multiple <<= 1
                temp <<= 1
            quotient += multiple
            dividend -= temp
        return -quotient if negative else quotient


if __name__ == "__main__":
    s = Solution()
    dividend = 7
    divisor = -3
    result = s.divide(dividend, divisor)
    print(result)
