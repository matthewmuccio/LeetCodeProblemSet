#!/usr/bin/env python3


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        a = len(s1)
        b = len(s2)
        c = len(s3)
        
        if a + b != c: return False
        
        queue = [(0, 0)]
        visited = set((0, 0))
        
        while queue:
            x, y = queue.pop(0)
            
            if x + y == c: return True
            
            if x + 1 <= a and s1[x] == s3[x + y] and (x + 1, y) not in visited:
                queue.append((x + 1, y))
                visited.add((x + 1, y))
                
            if y + 1 <= b and s2[y] == s3[x + y] and (x, y + 1) not in visited:
                queue.append((x, y + 1))
                visited.add((x, y + 1))
                
        return False


if __name__ == "__main__":
    s = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    result = s.isInterleave(s1, s2, s3)
    print(result)
