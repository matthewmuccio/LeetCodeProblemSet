#!/usr/bin/env python3


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        self.result = []
        self.findComb(candidates, [], target)
        return self.result

    def findComb(self, arr, curr, target):
        if not target:
            self.result.append(curr)
            return
        else:
            for i in range(len(arr)):
                if target - arr[i] < 0:
                    break
                else:
                    self.findComb(arr[i:], curr + [arr[i]], target - arr[i])
        return


if __name__ == "__main__":
    s = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    result = s.combinationSum(candidates, target)
    print(result)
