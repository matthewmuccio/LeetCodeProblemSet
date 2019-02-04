#!/usr/bin/env python3


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l = 0
        r = n - 1
        water = 0
        minHeight = 0

        while l < r:
            while l < r and height[l] <= minHeight:
                water += minHeight - height[l]
                l += 1

            while r > l and height[r] <= minHeight:
                water += minHeight - height[r]
                r -= 1

            minHeight = min(height[l], height[r])

        return water


if __name__ == "__main__":
    s = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = s.trap(height)
    print(result)
