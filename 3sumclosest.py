#!/usr/bin/env python3


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        res = nums[0] + nums[1] + nums[2]
        gap = abs(target - res)
        ln = len(nums)

        for i in range(ln):
            l = i + 1
            r = ln - 1

            while (l < r):
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                elif abs(target - s) < gap:
                    res = s
                    gap = abs(target - s)
                elif s < target:
                    l += 1
                elif s > target:
                    r -= 1
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [-1, 2, 1, -4]
    target = 1
    result = s.threeSumClosest(nums, target)
    print(result)
