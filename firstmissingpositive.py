#!/usr/bin/env python3


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        n = len(nums)

        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(len(nums)):
            nums[nums[i] % n] += n
        for i in range(1, len(nums)):
            if nums[i] / n == 0:
                return i

        return n


if __name__ == "__main__":
    s = Solution()
    nums = [3, 4, -1, 1]
    result = s.firstMissingPositive(nums)
    print(result)
