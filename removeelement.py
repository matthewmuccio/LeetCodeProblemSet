#!/usr/bin/env python3


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j


if __name__ == "__main__":
    s = Solution()
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    result = s.removeElement(nums, val)
    print(result)
