# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        list_sum = []

        def dfs(node):
            if not node: return 0
            sum = dfs(node.left) + dfs(node.right) + node.val
            list_sum.append(sum)
            return sum

        total = dfs(root)
        ans = float('-inf')
        for sum in list_sum:
            ans = max(ans, sum*(total-sum))

        return ans % (10**9+7)