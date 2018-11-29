#!/usr/bin/env python3


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""
        rules = ((1000, "M"),
                 (900, "CM"),
                 (500, "D"),
                 (400, "CD"),
                 (100, "C"),
                 (90, "XC"),
                 (50, "L"),
                 (40, "XL"),
                 (10, "X"),
                 (9, "IX"),
                 (5, "V"),
                 (4, "IV"),
                 (1, "I"))

        for n, s in rules:
            while True:
                newnum = num - n
                if newnum >= 0:
                    result += s
                    num = newnum
                else:
                    break
        return result


if __name__ == "__main__":
    s = Solution()
    num = 58
    result = s.intToRoman(num)
    print(result)
