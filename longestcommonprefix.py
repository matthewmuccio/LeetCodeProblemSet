#!/usr/bin/env python3


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        min_len = min([len(s) for s in strs])
        for i in range(min_len, -1, -1):
            if len(set([s[0:i] for s in strs])) == 1:
                return strs[0][0:i]
        return ""


if __name__ == "__main__":
    s = Solution()
    strs = ["flower", "flow", "flight"]
    result = s.longestCommonPrefix(strs)
    print(result)
