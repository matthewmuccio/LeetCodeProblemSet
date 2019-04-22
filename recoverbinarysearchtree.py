#!/usr/bin/env python3


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.prev = TreeNode(float("-inf")) 
        
        def inorder(node):
            if node:
                inorder(node.left)
                
                if not self.first and self.prev.val >= node.val: self.first = self.prev
                if self.first and self.prev.val >= node.val: self.second = node
                    
                self.prev = node
                
                inorder(node.right)
                
        inorder(root)
        
        self.first.val, self.second.val = self.second.val, self.first.val


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.right = TreeNode(2)
    s.recoverTree(root)
    print(root)
