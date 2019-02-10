#!/usr/bin/env python3


class Solution(object):
    def spiralOrder(self, matrix):
        if matrix == []:
            return matrix

        t = 0
        r = len(matrix[0]) - 1
        b = len(matrix) - 1
        l = 0
        res = []

        while l < r and t < b:
            for i in range(l, r):
                res.append(matrix[t][i])
            for i in range(t, b):
                res.append(matrix[i][r])
            for i in range(r, l, -1):
                res.append(matrix[b][i])
            for i in range(b, t, -1):
                res.append(matrix[i][l])

            t += 1
            r -= 1
            b -= 1
            l += 1

        if l == r and t == b:
            res.append(matrix[t][l])
        elif l == r:
            for i in range(t, b + 1):
                res.append(matrix[i][l])
        elif t == b:
            for i in range(l, r + 1):
                res.append(matrix[t][i])

       	return res


if __name__ == "__main__":
    s = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = s.spiralOrder(matrix)
    print(result)
