# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        def dfs(root, tmp, sum):
            nonlocal res
            if not root:
                return 
            
            sum -= root.val
            if not root.left and not root.right and sum == 0:
                res.append(tmp + [root.val])
            dfs(root.left, tmp + [root.val], sum)
            dfs(root.right, tmp + [root.val], sum)
            return res
        
        dfs(root, [], sum)
        return res