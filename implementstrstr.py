#!/usr/bin/env python3


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.index(needle) if needle in haystack else -1


if __name__ == "__main__":
    s = Solution()
    haystack = "hello"
    needle = "ll"
    result = s.strStr(haystack, needle)
    print(result)
