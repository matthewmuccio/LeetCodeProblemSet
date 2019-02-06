#!/usr/bin/env python3


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        stack = [[(0, i)] for i in range(n)]
        res = []

        while stack:
            board = stack.pop()
            row = len(board)

            if row == n:
                res.append(["".join("Q" if i == c else "." for i in range(n)) for r, c in board])
            for col in range(n):
                if all(col != c and abs(row - r) != abs(col - c) for r, c in board):
                    stack.append(board + [(row, col)])

        return res


if __name__ == "__main__":
    s = Solution()
    n = 4
    result = s.solveNQueens(n)
    print(result)
