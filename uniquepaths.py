#!/usr/bin/env python3


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 0 or n <= 0: return 0
        if m == 1 or n == 1: return 1

        dp = [[1 for x in range(n)] for x in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[-1][-1]


if __name__ == "__main__":
    s = Solution()
    m = 3
    n = 2
    result = s.uniquePaths(m, n)
    print(result)
