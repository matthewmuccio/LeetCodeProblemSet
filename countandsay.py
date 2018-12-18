#!/usr/bin/env python3


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1: return "1"
        if n == 2: return "11"

        def countSay(s):
            output = ""
            count = 1

            for i in range(1, len(s)):
                if s[i - 1] == s[i]: count += 1
                else:
                    output += str(count) + s[i - 1]
                    count = 1
                if i == len(s) - 1: output += str(count) + s[i]
            return output

        dp = [""] * (n + 1)
        dp[1], dp[2] = "1", "11"

        for i in range(3, n + 1):
            count = 1
            dp[i] = countSay(dp[i - 1])

        return dp[n]


if __name__ == "__main__":
    s = Solution()
    n = 4
    result = s.countAndSay(n)
    print(result)
