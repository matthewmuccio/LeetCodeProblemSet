#!/usr/bin/env python3


class Solution(object):
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return lookup[target - num], i
            lookup[num] = i


if __name__ == "__main__":
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = s.twoSum(nums, target)
    print(result)
