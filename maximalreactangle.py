#!/usr/bin/env python3


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        
        n = len(matrix[0])
        height = [0] * (n + 1)
        result = 0
        
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == "1" else 0
                
            stack = [-1]
            
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    result = max(result, h * w)
                    
                stack.append(i)
                
        return result


if __name__ == "__main__":
    s = Solution()
    matrix = [
      ["1","0","1","0","0"],
      ["1","0","1","1","1"],
      ["1","1","1","1","1"],
      ["1","0","0","1","0"]
    ]
    result = s.maximalRectangle(matrix)
    print(result)
