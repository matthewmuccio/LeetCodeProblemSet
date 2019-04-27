#!/usr/bin/env python3


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSym(l, r):
            if l and r and l.val == r.val: 
                return isSym(l.left, r.right) and isSym(l.right, r.left)
            return l == r
        
        return not root or isSym(root.left, root.right)


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    result = s.isSymmetric(root)
    print(result)
