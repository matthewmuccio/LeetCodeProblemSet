#!/usr/bin/env python3


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        s1 = list(s)
        maxlen = 0
        stack.append(-1)

        for i in range(len(s1)):
            if s1[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxlen = max(maxlen, i - stack[-1])

        return maxlen


if __name__ == "__main__":
    s = Solution()
    s1 = ")()())"
    result = s.longestValidParentheses(s1)
    print(result)
