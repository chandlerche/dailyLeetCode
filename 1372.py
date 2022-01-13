# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node: TreeNode, depth=0, ward=-1):
            if not node:
                return

            self.ans = max(self.ans, depth)
            if ward == -1:
                dfs(node.left, depth + 1, 0)
                dfs(node.right, depth + 1, 1)
            elif ward == 0:
                dfs(node.left, 1, 0)
                dfs(node.right, depth + 1, 1)
            else:
                dfs(node.left, depth + 1, 0)
                dfs(node.right, 1, 1)

        dfs(root)
        return self.ans