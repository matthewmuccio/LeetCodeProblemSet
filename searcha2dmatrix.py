#!/usr/bin/env python3


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        
        for row in matrix:
            for i in range(len(row)):
                if row[0] <= target <= row[-1] and target in row:
                    return True
        
        return False


if __name__ == "__main__":
    s = Solution()
    nums = [2, 7, 11, 15]
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 3
    result = s.searchMatrix(matrix, target)
    print(result)
