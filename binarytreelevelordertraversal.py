#!/usr/bin/env python3


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        
        res = []
        level = [root]
        
        while level:
            res.append([node.val for node in level])
            temp = []
            
            for node in level:
                temp.extend([node.left, node.right])
                
            level = [leaf for leaf in temp if leaf]

        return res


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    result = s.levelOrder(root)
    print(result)
