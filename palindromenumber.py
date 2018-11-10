#!/usr/bin/env python3


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x)[::-1] == str(x)


if __name__ == "__main__":
    s = Solution()
    x = 121
    result = s.isPalindrome(x)
    print(result)
