#!/usr/bin/env python3


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        l = sum(([(col, i), (j, col), (i / 3, j / 3, col)]
                    for i, row in enumerate(board)
                    for j, col in enumerate(row)
                    if col != "."), [])

        return len(l) == len(set(l))


if __name__ == "__main__":
    s = Solution()
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    result = s.isValidSudoku(board)
    print(result)
