# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        lh, rh = self.__getHeight(root.left), self.__getHeight(root.right)
        if lh == rh:  # 左右子树高度相同，说明左子树必满 则节点数=左子树节点 + root节点(=1) + 递归找右子树
            return (pow(2, lh) - 1) + 1 + self.countNodes(root.right)
        else:  # 左子树比右子树高，说明右子树必满 同理
            return (pow(2, rh) - 1) + 1 + self.countNodes(root.left)

    def __getHeight(self, root):
        ret = 0
        while root:
            ret += 1
            root = root.left
        return ret