#!/usr/bin/env python3


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol = ["I", "V", "X", "L", "C", "D", "M"]
        value = [1, 5, 10, 50, 100, 500, 1000]
        d = dict(zip(symbol, value))
        res = 0
        temp = 0
        for c in s:
            if d[c] > temp:
                res -= (temp << 1)
            res += d[c]
            temp = d[c]
        return res


if __name__ == "__main__":
    s = Solution()
    s1 = "LVIII"
    result = s.romanToInt(s1)
    print(result)
