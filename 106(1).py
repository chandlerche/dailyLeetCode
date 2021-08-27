# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    pInorder = 0
    pPostorder = 0

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.pInorder = len(inorder) - 1
        self.pPostorder = len(postorder) - 1
        return self.helper(inorder , postorder , None)

    def helper(self , inorder , postorder , end):
        if self.pPostorder < 0:
            return None
        root = TreeNode(postorder[self.pPostorder])
        self.pPostorder -= 1
        if inorder[self.pInorder] != root.val: #这句代码的意思相当于inorder存在右子树的话
            root.right = self.helper(inorder , postorder , root) #root是例子中的3
        #此时右子树已经一条路走到黑走完了，所以我们已经得到inorder的最后一个了，所以减一
        self.pInorder -= 1
        # 左子树该怎么走？因为我们end一开始为空，不这么写永远得不到左子树
        if end == None or inorder[self.pInorder] != end.val:
            root.left = self.helper(inorder , postorder , end)
        return root