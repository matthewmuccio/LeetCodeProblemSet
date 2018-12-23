#!/usr/bin/env python3


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        visited = [False] * len(nums)

        def permutate(nums):
            if len(visited) == len(nums) and all(visited):
                return [[]]
            ret = []

            for i in range(len(nums)):
                if visited[i]:
                    continue
                visited[i] = True

                for n in permutate(nums):
                    ret.append([nums[i]] + n)
                visited[i] = False

            return ret

        return permutate(nums)


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3]
    result = s.permute(nums)
    print(result)
