#!/usr/bin/env python3


class Solution(object):
    def myAtoi(self, str):
        """
        :type s: str
        :rtype: bool
        """
        min = -2147483648
        max = 2147483647
        res = ""
        str_list = list(str.strip())
        for index, char in enumerate(str_list):
            if len(res) > 0 and not char.isdigit():
                break
            elif index == 1 and not char.isdigit():
                return 0
            elif char == '+':
                continue
            elif char.isdigit() or char == '-':
                res += char
            else:
                return 0
        if res == '-' or len(res) == 0:
            return 0
        res = int(res)
        if res > max:
            return max
        elif res < min:
            return min
        return res


if __name__ == "__main__":
    s = Solution()
    str = "4193 with words"
    result = s.myAtoi(str)
    print(result)
