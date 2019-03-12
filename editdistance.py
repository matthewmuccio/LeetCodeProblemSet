#!/usr/bin/env python3


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = len(word1) + 1
        l2 = len(word2) + 1
        dp = [i for i in range(l2)]
        pre = 0
        for i in range(1, l1):
            pre = i - 1
            dp[0] = i
            for j in range(1, l2):
                buff = dp[j]
                dp[j] = min(dp[j] + 1, dp[j - 1] + 1, pre + (word1[i - 1] != word2[j - 1]))
                pre = buff

        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    word1 = "intention"
    word2 = "execution"
    result = s.minDistance(word1, word2)
    print(result)
