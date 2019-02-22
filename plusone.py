#!/usr/bin/env python3


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0

        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits) - 1 - i))

        return [int(i) for i in str(num + 1)]


if __name__ == "__main__":
    s = Solution()
    digits = [1, 2, 3]
    result = s.plusOne(digits)
    print(result)
