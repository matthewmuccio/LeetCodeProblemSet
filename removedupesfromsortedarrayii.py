#!/usr/bin/env python3


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        
        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
                
        return i


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    result = s.removeDuplicates(nums)
    print(result)
