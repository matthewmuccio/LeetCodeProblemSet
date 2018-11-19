#!/usr/bin/env python3


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        i = 0
        m = {}
        for j in range(len(s)):
            if s[j] in m:
                i = max(m[s[j]], i)
            ans = max(ans, j - i + 1)
            m[s[j]] = j + 1
        return ans


if __name__ == "__main__":
    s = Solution()
    s1 = "abcabcbb"
    result = s.lengthOfLongestSubstring(s1)
    print(result)
