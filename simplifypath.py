#!/usr/bin/env python3


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        places = [p for p in path.split("/") if p != "." and p != ""]
        stack = []

        for p in places:
            if p == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)

        return "/" + "/".join(stack)


if __name__ == "__main__":
    s = Solution()
    path = "/a/../../b/../c//.//"
    result = s.simplifyPath(path)
    print(result)
