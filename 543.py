# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def deapth(node: TreeNode) -> int:
            nonlocal ma
            if not node:
                return 0
            l = deapth(node.left)
            r = deapth(node.right)
            ma = max(l + r, ma)
            return max(l, r) + 1
        ma = 0
        deapth(root)
        return ma