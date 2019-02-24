#!/usr/bin/env python3


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c = '0'
        output = ''

        b = '0' * (len(a) - len(b)) + b if len(a) > len(b) else b
        a = '0' * (len(b) - len(a)) + a if len(b) > len(a) else a

        for i in range(len(a) - 1, -1, -1):
            count = (a[i] + b[i] + c).count('1')
            sm = '1' if count % 2 else '0'
            c = '0' if count < 2 else '1'
            output = sm + output

        return c + output if c == '1' else output


if __name__ == "__main__":
    s = Solution()
    a = "11"
    b = "1"
    result = s.addBinary(a, b)
    print(result)
