#!/usr/bin/env python3


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def insert(nums, target):
            nums.append(target)
            return sorted(nums).index(target)
        return nums.index(target) if target in nums else insert(nums, target)


if __name__ == "__main__":
    s = Solution()
    nums = [1, 3, 5, 6]
    target = 5
    result = s.searchInsert(nums, target)
    print(result)
