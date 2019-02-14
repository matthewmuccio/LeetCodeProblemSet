#!/usr/bin/env python3


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.rstrip(" ").split(" ")[-1])


if __name__ == "__main__":
    s = Solution()
    s1 = "Hello World"
    result = s.lengthOfLastWord(s1)
    print(result)
