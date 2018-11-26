#!/usr/bin/env python3


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        mn = -2147483648
        mx = 2147483647
        res = ""
        str_list = list(str.strip())
        for i, s in enumerate(str_list):
            if len(res) > 0 and not s.isdigit():
                break
            elif i == 1 and not s.isdigit():
                return 0
            elif s == "+":
                continue
            elif s.isdigit() or s == "-":
                res += s
            else:
                return 0
        if res == "-" or len(res) == 0:
            return 0
        res = int(res)
        if res > mx:
            return mx
        elif res < mn:
            return mn
        return res


if __name__ == "__main__":
    s = Solution()
    str = "     -42"
    result = s.myAtoi(str)
    print(result)
