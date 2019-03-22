#!/usr/bin/env python3


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        
        for num in nums:
            res += [i + [num] for i in res]
            
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3]
    result = s.subsets(nums)
    print(result)
