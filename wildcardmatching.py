#!/usr/bin/env python3


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        l = len(s)

        if len(p) - p.count("*") > l:
            return False

        dp = [True] + [False] * l

        for letter in p:
            new_dp = [dp[0] and letter == "*"]
            if letter == "*":
                for j in range(l):
                    new_dp.append(new_dp[-1] or dp[j + 1])
            elif letter == "?":
                new_dp += dp[:l]
            else:
                new_dp += [dp[j] and s[j] == letter for j in range(l)]
            dp = new_dp

        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    s1 = "aa"
    p = "*"
    result = s.isMatch(s1, p)
    print(result)
