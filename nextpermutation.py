#!/usr/bin/env python3


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                break
        if i == 1 and nums[0] > nums[1]:
            nums.sort()
        else:
            smallestIndex = i
            for j in range(i + 1, n):
                if nums[j] < nums[smallestIndex] and nums[j] > nums[i-1]:
                    smallestIndex = j
            nums[i - 1], nums[smallestIndex] = nums[smallestIndex], nums[i - 1]
            nums[i:] = sorted(nums[i:])


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3]
    s.nextPermutation(nums)
    print(nums)
