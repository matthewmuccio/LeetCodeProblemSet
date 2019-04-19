#!/usr/bin/env python3


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True

        def isBSTHelper(node, lower_limit, upper_limit):
            if lower_limit != None and node.val <= lower_limit: return False
            if upper_limit != None and upper_limit <= node.val: return False

            left = isBSTHelper(node.left, lower_limit, node.val) if node.left else True
            
            if left:
                right = isBSTHelper(node.right, node.val, upper_limit) if node.right else True
                return right
            else:
                return False
        
        return isBSTHelper(root, None, None)


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    result = s.isValidBST(root)
    print(result)
