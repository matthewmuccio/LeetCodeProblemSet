#!/usr/bin/env python3


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]

        for n in nums:
            new_res = []

            for l in result:

                for i in range(len(l) + 1):
                    new_res.append(l[:i] + [n] + l[i:])
                    if i < len(l) and l[i] == n:
                        break
            result = new_res

        return result


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 2]
    result = s.permuteUnique(nums)
    print(result)
