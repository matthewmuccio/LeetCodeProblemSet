#!/usr/bin/env python3


from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""

        d = Counter(t)
        required = len(d)
        l, r = 0, 0
        formed = 0
        window_counts = {}
        
        ans = float("inf"), None, None

        while r < len(s):
            c = s[r]
            window_counts[c] = window_counts.get(c, 0) + 1
            if c in d and window_counts[c] == d[c]:
                formed += 1

            while l <= r and formed == required:
                c = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                window_counts[c] -= 1
                if c in d and window_counts[c] < d[c]:
                    formed -= 1
                l += 1
                
            r += 1
            
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


if __name__ == "__main__":
    s = Solution()
    s1 = "ADOBECODEBANC"
    t = "ABC"
    result = s.minWindow(s1, t)
    print(result)
