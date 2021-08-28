# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        if not preorder: return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        idx = postorder.index(preorder[1])+1
        root.left = self.constructFromPrePost(preorder[1:idx+1], postorder[:idx])
        root.right = self.constructFromPrePost(preorder[idx+1:], postorder[idx:-1])
        return root