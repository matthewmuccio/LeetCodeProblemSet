#!/usr/bin/env python3


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        A = [[0] * n for _ in range(n)]
        i, j = 0, 0
        di, dj = 0, 1

        for k in range(n * n):
            A[i][j] = k + 1

            if A[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di
            i += di
            j += dj

        return A


if __name__ == "__main__":
    s = Solution()
    n = 3
    result = s.generateMatrix(n)
    print(result)
