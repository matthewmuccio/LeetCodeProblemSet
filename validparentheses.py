#!/usr/bin/env python3


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mp = { ")" : "(", "}" : "{", "]" : "[" }

        for c in s:
            if c in mp:
                top = stack.pop() if stack else "#"
                if mp[c] != top:
                    return False
            else:
                stack.append(c)
        return not stack


if __name__ == "__main__":
    s = Solution()
    str = "()[]{}"
    result = s.isValid(str)
    print(result)
