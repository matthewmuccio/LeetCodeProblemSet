#!/usr/bin/env python3


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        curr_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)

        return max_sum


if __name__ == "__main__":
    s = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = s.maxSubArray(nums)
    print(result)
