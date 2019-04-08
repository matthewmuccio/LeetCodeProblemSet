#!/usr/bin/env python3


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        
        nums.sort()
        
        for num in nums: 
            res += [ i + [num] for i in res if i + [num] not in res]
            
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 2]
    result = s.subsetsWithDup(nums)
    print(result)
