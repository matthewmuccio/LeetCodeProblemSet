#!/usr/bin/env python3


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = True if i == len(s) else False
                else:
                    first_match = i < len(s) and p[j] in {s[i], "."}

                    if j + 1 < len(p) and p[j + 1] == "*":
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)


if __name__ == "__main__":
    s = Solution()
    s1 = "aa"
    p = "a*"
    result = s.isMatch(s1, p)
    print(result)
