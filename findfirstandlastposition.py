#!/usr/bin/env python3


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Find the index of the left-most appearance of target.
        # If it does not appear, return [-1, -1] early.
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        else:
            return [-1, -1]

        # Find the index of the right-most appearance of target
        # (by reverse iteration).
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] == target:
                right_idx = j
                break

        return [left_idx, right_idx]


if __name__ == "__main__":
    s = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    result = s.searchRange(nums, target)
    print(result)
