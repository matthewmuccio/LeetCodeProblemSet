#!/usr/bin/env python3


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0": return "0"

        num1 = [int(n) for n in num1]
        num2 = [int(n) for n in num2]
        out = [0] * (len(num1) + len(num2) - 1)

        for i, n1 in enumerate(reversed(num1)):
            carry = 0

            for j, n2 in enumerate(reversed(num2)):
                if len(out) <= i + j:
                    out.append(0)
                num = n1 * n2 + carry + out[i + j]
                carry = num // 10
                out[i + j] = num % 10

            if carry:
                if len(out) <= i + len(num2):
                    out.append(0)
                out[i + len(num2)] += carry

        return "".join(reversed([str(n) for n in out]))


if __name__ == "__main__":
    s = Solution()
    num1 = "123"
    num2 = "456"
    result = s.multiply(num1, num2)
    print(result)
