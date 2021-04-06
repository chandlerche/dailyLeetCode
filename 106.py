# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return None
        root = TreeNode(postorder[-1])#创建树
        n = inorder.index(root.val)
        root.left = self.buildTree(inorder[:n],postorder[:n])
        root.right = self.buildTree(inorder[n+1:],postorder[n:-1])
        return root