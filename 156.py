class Solution(Object):

    def upsideDownBinaryTree(self , root):
        if not root or (root.left == None and root.right == None):
            return root
        newRoot = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right #把根结点左节点作为新的根结点，它的左节点连上原右节点
        root.left.right = root # 它的右节点连上原根结点

        root.left = None #解放原根结点的所有联系
        root.right = None

        return newRoot