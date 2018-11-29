#!/usr/bin/env python3


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0
        right = n - 1
        water = 0
        for i in range(n - 1, -1, -1):
            if height[left] < height[right]:
                water = max(height[left] * i, water)
                left += 1
            else:
                water = max(height[right] * i, water)
                right -= 1
        return water


if __name__ == "__main__":
    s = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = s.maxArea(height)
    print(result)
