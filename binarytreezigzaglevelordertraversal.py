#!/usr/bin/env python3


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        
        res = []
        level = [root]
        direction = 1
        
        while level:
            res.append([node.val for node in level][::direction])
            direction *= -1
            level = [child for node in level for child in (node.left, node.right) if child]
            
        return res


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    result = s.zigzagLevelOrder(root)
    print(result)
