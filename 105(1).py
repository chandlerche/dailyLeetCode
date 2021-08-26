# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.helper(0 , 0 , len(inorder) - 1 , preorder , inorder)
    
    def helper(self , preStart , inStart , inEnd , preorder , inorder):
        if preStart > len(preorder) - 1 or inStart > inEnd:
            return None
        root = TreeNode(preorder[preStart]) #首先，preorder的第一个一定是根结点
        inIndex = 0
        for i in range(inStart , inEnd + 1):
            if inorder[i] == root.val:
                inIndex = i #找到中序遍历中根结点的index
        # 最后两句是重中之重，中序中，左子树一定在根结点的前面/前一位开始
        # 因为右子树始终是最后遍历的，所以左子树的个数是相等的，右子树一定是把它们都遍历完了才轮到
        root.left = self.helper(preStart + 1 , inStart , inIndex - 1 , preorder , inorder)
        root.right = self.helper(preStart + (inIndex - inStart) + 1 , inIndex + 1 , inEnd , preorder , inorder)
        return root

'''
首先要知道一个结论，前序/后序+中序序列可以唯一确定一棵二叉树，所以自然而然可以用来建树。
看一下前序和中序有什么特点，前序1,2,4,7,3,5,6,8 ，中序4,7,2,1,5,3,8,6；
有如下特征：
1. 前序中左起第一位1肯定是根结点，我们可以据此找到中序中根结点的位置rootin；
2. 中序中根结点左边就是左子树结点，右边就是右子树结点，即[左子树结点，根结点，右子树结点]，我们就可以得出左子树结点个数为int left = rootin - leftin;；
3. 前序中结点分布应该是：[根结点，左子树结点，右子树结点]；
4. 根据前一步确定的左子树个数，可以确定前序中左子树结点和右子树结点的范围；
5. 如果我们要前序遍历生成二叉树的话，下一层递归应该是：
    * 左子树：root->left = pre_order(前序左子树范围，中序左子树范围，前序序列，中序序列);；
    * 右子树：root->right = pre_order(前序右子树范围，中序右子树范围，前序序列，中序序列);。
6. 每一层递归都要返回当前根结点root；
'''