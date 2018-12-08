#!/usr/bin/env python3


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        s = ""
        self.parenthesisHelper(res, s, n, n)
        return res

    def parenthesisHelper(self,res,s,n,m):
        if n > m:
            return
        if n == 0 and m == 0:
            res.append(s)
        if n > 0:
            temp = s + "("
            self.parenthesisHelper(res, temp, n - 1, m)
        if m > 0:
            temp = s + ")"
            self.parenthesisHelper(res, temp, n, m - 1)


if __name__ == "__main__":
    s = Solution()
    n = 3
    result = s.generateParenthesis(n)
    print(result)
