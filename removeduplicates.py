#!/usr/bin/env python3


class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0: return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


if __name__ == "__main__":
    s = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    result = s.removeDuplicates(nums)
    print(result)
