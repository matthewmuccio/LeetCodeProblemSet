#!/usr/bin/env python3


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [-1]
        result = 0
        
        heights.append(0)

        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                result = max(result, h * w)
            stack.append(i)
            
        heights.pop()
        
        return result


if __name__ == "__main__":
    s = Solution()
    heights = [2, 1, 5, 6, 2, 3]
    result = s.largestRectangleArea(heights)
    print(result)
