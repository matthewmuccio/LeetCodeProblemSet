#!/usr/bin/env python3


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        output = []
        n = len(s)
        cycle = 2 * numRows - 2
        for i in range(numRows):
            j = 0
            while j + i < n:
                output.append(s[j + i])
                if i != 0 and i != numRows - 1 and j + cycle - i < n:
                    output.append(s[j + cycle - i])
                j += cycle
        return "".join(output)


if __name__ == "__main__":
    s = Solution()
    s1 = "PAYPALISHIRING"
    result = s.convert(s1, 3)
    print(result)
