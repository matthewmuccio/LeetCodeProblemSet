#!/usr/bin/env python3


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_max_reach = 0
        current_max_reach = 0
        num_jump = 0
        i = 0

        while current_max_reach < len(nums) - 1:
            while i <= last_max_reach:
                current_max_reach = max(i + nums[i], current_max_reach)
                i += 1
            if last_max_reach == current_max_reach:
                return -1
            last_max_reach = current_max_reach
            num_jump += 1

        return num_jump


if __name__ == "__main__":
    s = Solution()
    nums = [2, 3, 1, 1, 4]
    result = s.jump(nums)
    print(result)
