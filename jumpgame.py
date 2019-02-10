#!/usr/bin/env python3


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0
        n = len(nums)

        for i, x in enumerate(nums):
            if max_reach < i:
                return False
            if max_reach >= n - 1:
                return True
            max_reach = max(max_reach, i + x)


if __name__ == "__main__":
    s = Solution()
    nums = [2, 3, 1, 1, 4]
    result = s.canJump(nums)
    print(result)
