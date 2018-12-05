#!/usr/bin/env python3


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def findNsum(nums, target, N, cur):
            # If it's impossible to get target (if minimum/maximum possible sum (every element is first element) >/< target).
            if len(nums) < N or N < 2 or nums[0] * N > target or nums[-1] * N < target:
                return
            # 2Sum problem.
            if N == 2:
                l, r = 0, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        res.append(cur + [nums[l], nums[r]])
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            # Reduce to N - 1 sum problem.
            else:
                for i in range(len(nums) - N + 1):
                    if i == 0 or nums[i - 1] != nums[i]:
                        findNsum(nums[i + 1 :], target - nums[i], N - 1, cur + [nums[i]])
        res = []
        findNsum(sorted(nums), target, 4, [])
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    result = s.fourSum(nums, target)
    print(result)
