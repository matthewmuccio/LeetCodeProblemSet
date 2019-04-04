#!/usr/bin/env python3


class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n = len(s1)
        m = len(s2)
        
        if n != m or sorted(s1) != sorted(s2): return False
        if n < 4 or s1 == s2: return True
        
        f = self.isScramble
        
        for i in range(1, n):
            if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or \
               f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
                return True
            
        return False


if __name__ == "__main__":
    s = Solution()
    s1 = "great"
    s2 = "rgeat"
    result = s.isScramble(s1, s2)
    print(result)
