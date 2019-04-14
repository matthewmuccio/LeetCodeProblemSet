#!/usr/bin/env python3


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def dfs(l, r):
            if r < l: return [None]
            
            res = []
            
            for i in range(l, r + 1):
                left = dfs(l, i - 1)
                right = dfs(i + 1, r)
                
                for leftNode in left:
                    for rightNode in right:
                        new = TreeNode(i)
                        new.left = leftNode
                        new.right = rightNode
                        res.append(new)
            return res
        
        res = dfs(1, n)
        
        return [] if res == [None] else res


if __name__ == "__main__":
    s = Solution()
    n = 3
    result = s.generateTrees(n)
    print(result)
