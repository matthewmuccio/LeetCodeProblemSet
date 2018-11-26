#!/usr/bin/env python3


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            temp = self.helper(s, i, i)
            if len(temp) > len(res):
                res = temp
            temp = self.helper(s, i, i + 1)
            if len(temp) > len(res):
                res = temp
        return res

    # Gets the longest palindrome.
    # l, r are the middle indices from inner to outer.
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]


if __name__ == "__main__":
    s = Solution()
    s1 = "babad"
    result = s.longestPalindrome(s1)
    print(result)
