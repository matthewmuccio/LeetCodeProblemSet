#!/usr/bin/env python3


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        
        for i in range(n):
            res += [x + pow(2, i) for x in reversed(res)]
            
        return res


if __name__ == "__main__":
    s = Solution()
    n = 2
    result = s.grayCode(n)
    print(result)
