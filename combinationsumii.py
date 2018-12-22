#!/usr/bin/env python3

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        dp = [set() for i in range(target + 1)]
        dp[0].add(())

        for num in candidates:
            for i in range(target, num - 1, -1):
                for prev in dp[i - num]:
                    dp[i].add(prev + (num,))

        return list(dp[-1])


if __name__ == "__main__":
    s = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    result = s.combinationSum2(candidates, target)
    print(result)
