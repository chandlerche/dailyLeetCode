# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.res = -float('inf')
        self.helper(root)
        return self.res

    def helper(self , root):
        if not root: return 0
        left = max(0 , self.helper(root.left))
        right = max(0 , self.helper(root.right))
        self.res = max(self.res , left + right +root.val)
        return max(left , right) + root.val